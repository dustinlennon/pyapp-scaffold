
import jinja2
from scaffold.params.base_mixin import BaseMixin
from scaffold.params import _printf_debug

class JinjaTemplateMixin(BaseMixin):
  def assign_args(self, args):
    _printf_debug("JinjaTemplateMixin.assign_args")
    super().assign_args(args)
    self._j2env = jinja2.Environment(
      loader = jinja2.FileSystemLoader(str(args.template_path))
    )

  def get_template(self, name, parent = None, globals = None) -> jinja2.Template:
    return self._j2env.get_template(name, parent = parent, globals = globals)
