from jinja2 import Environment, FileSystemLoader
import os
import uuid
import tempfile

template_env = Environment(loader=FileSystemLoader("templates"))

def build_etl_script(config: dict) -> str:
    template = template_env.get_template("etl_template.j2")
    rendered_code = template.render(config=config)

    temp_dir = tempfile.gettempdir()
    output_path = os.path.join(temp_dir, f"generated_etl_{uuid.uuid4().hex}.py")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_code)
    
    return rendered_code
