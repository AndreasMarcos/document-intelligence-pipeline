from dataclasses import dataclass, field


@dataclass
class Document:
    page_content: str
    metadata: dict = field(default_factory=dict)


@dataclass
class InsightReport:
    filename: str = ""
    summary: str = ""
    entities: dict = field(default_factory=dict)
    nlp_analysis: dict = field(default_factory=dict)
    literature_context: str = ""
    final_report: str = ""
    steps: list[dict] = field(default_factory=list)