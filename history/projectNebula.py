"""Project Nebula.

A tiny experimental toolkit for turning ordinary ideas into working prototypes.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Pipeline:
    mode: str = "fast"
    output_dir: str = "output"
    debug: bool = False

    def run(self, text: str) -> dict:
        result = {
            "mode": self.mode,
            "input": text,
            "output": text.strip().upper(),
        }
        if self.debug:
            result["debug"] = True
        return result


def load_environment(config: dict | None = None) -> Pipeline:
    config = config or {}
    return Pipeline(
        mode=config.get("NEBULA_MODE", "fast"),
        output_dir=config.get("NEBULA_OUTPUT", "output"),
        debug=bool(config.get("NEBULA_DEBUG", False)),
    )


def save_result(result: dict, output_dir: str = "output") -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / "result.txt"
    file_path.write_text(str(result), encoding="utf-8")
    return file_path


def main() -> None:
    pipeline = Pipeline(mode="fast")
    result = pipeline.run("hello world")
    save_result(result, pipeline.output_dir)
    print(result)


if __name__ == "__main__":
    main()