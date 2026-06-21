from __future__ import annotations
from pathlib import Path
from typing import Dict

from jinja2 import Environment, FileSystemLoader, TemplateNotFound, select_autoescape

TEMPLATES_PATH = Path(__file__).resolve().parent.parent / "templates" / "email"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_PATH)),
    autoescape=select_autoescape(["html", "xml"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


class EmailTemplateError(Exception):
    pass


class EmailTemplateRenderer:
    def __init__(self, environment: Environment = env) -> None:
        self.environment = environment

    def render_html(self, template_name: str, context: Dict[str, str]) -> str:
        return self._render(template_name + ".html", context)

    def render_text(self, template_name: str, context: Dict[str, str]) -> str:
        return self._render(template_name + ".txt", context)

    def _render(self, template_name: str, context: Dict[str, str]) -> str:
        try:
            template = self.environment.get_template(template_name)
            return template.render(**context)
        except TemplateNotFound as exc:
            raise EmailTemplateError(
                f"Template '{template_name}' not found in {TEMPLATES_PATH}"
            ) from exc
        except Exception as exc:
            raise EmailTemplateError(
                f"Unable to render template '{template_name}': {exc}"
            ) from exc
