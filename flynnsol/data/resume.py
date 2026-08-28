"""Single source of truth for resume/bio content, shared by the Home and Resume pages."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Role:
    title: str
    start: str
    end: str
    bullets: list[str]


@dataclass(frozen=True)
class CompanyBlock:
    company: str
    location: str
    roles: list[Role]  # newest role first


@dataclass(frozen=True)
class EducationEntry:
    school: str
    program: str
    dates: str


@dataclass(frozen=True)
class Certification:
    name: str
    issuer: str
    date: str


@dataclass(frozen=True)
class ResumeData:
    name: str
    title: str
    email: str
    github: str
    gitlab: str
    status: str
    summary: str
    short_bio: str
    skills: list[str] = field(default_factory=list)
    experience: list[CompanyBlock] = field(default_factory=list)
    education: list[EducationEntry] = field(default_factory=list)
    certifications: list[Certification] = field(default_factory=list)


RESUME = ResumeData(
    name="Flynn Sol",
    title="Software Engineer",
    email="hello@flynnsol.com",
    github="github.com/flynnsol",
    gitlab="gitlab.com/flynnsol",
    status="Open to work — remote / hybrid",
    summary=(
        "Software Engineer with a 4-year track record inside Huntress's IT and "
        "security organization — progressing from sales into help desk, IT "
        "operations, and now backend engineering using Ruby on Rails. Brings a "
        "rare combination of hands-on systems/networking depth and shipping "
        "product code, plus firsthand fluency in how security operations teams "
        "actually work."
    ),
    short_bio=(
        "I ship backend code at a hypergrowth cybersecurity company — and I got "
        "here through help desk tickets, IT ops, and a lot of curiosity about "
        "how the systems I supported actually worked underneath."
    ),
    skills=[
        "Ruby",
        "Ruby on Rails",
        "Python",
        "TypeScript",
        "Rust",
        "Java",
        "Usage-Based Billing",
        "SQL",
        "Git",
        "Linux",
        "Networking",
        "REST APIs",
        "Systems Administration",
        "Debugging",
        "Agile",
        "Claude",
        "Gemini",
    ],
    experience=[
        CompanyBlock(
            company="Huntress",
            location="Remote",
            roles=[
                Role(
                    title="Software Engineer",
                    start="Nov 2025",
                    end="Present",
                    bullets=[
                        "Work in Huntress' billing system (Ruby on Rails), implementing "
                        "usage calculation logic and new billing types to support product "
                        "launches at a hypergrowth cybersecurity company.",
                        "Build the billing plumbing for new products as they ship, "
                        "translating pricing and packaging decisions into accurate, "
                        "auditable usage-based charges.",
                        "Bring direct IT operations and help desk experience to "
                        "engineering work, closing the gap between how the product is "
                        "built and how it's actually used by security teams.",
                    ],
                ),
                Role(
                    title="Information Technology Operations Specialist",
                    start="Jul 2025",
                    end="Nov 2025",
                    bullets=[
                        "Configured and deployed MDM for multiple software rollouts.",
                        "Led a full SSO migration to a new identity provider.",
                    ],
                ),
                Role(
                    title="IT Help Desk Administrator",
                    start="Feb 2024",
                    end="Aug 2025",
                    bullets=[
                        "Redesigned the company's employee onboarding process end-to-end "
                        "and built a cross-department workflow to run it, helping onboard "
                        "400+ employees faster and more efficiently.",
                    ],
                ),
                Role(
                    title="Sales Development Representative",
                    start="Jun 2022",
                    end="Feb 2024",
                    bullets=[
                        "Assisted in bringing in over $800K in net new closed-won ARR "
                        "before moving internally into IT and engineering.",
                    ],
                ),
            ],
        ),
        CompanyBlock(
            company="EyeKraft",
            location="St. Cloud, MN",
            roles=[
                Role(
                    title="IT Technician",
                    start="Sep 2021",
                    end="Jun 2022",
                    bullets=[
                        "Provided on-site technical support and systems maintenance, "
                        "building the troubleshooting fundamentals that carried into a "
                        "remote IT and engineering career.",
                    ],
                ),
            ],
        ),
        CompanyBlock(
            company="Early Career",
            location="",
            roles=[
                Role(
                    title="Retail & Logistics Operations",
                    start="2016",
                    end="2021",
                    bullets=[
                        "Additional early experience in retail and logistics operations.",
                    ],
                ),
            ],
        ),
    ],
    education=[
        EducationEntry(
            school="Southern New Hampshire University",
            program="Computer Programming Certificate, Computer Science",
            dates="Sep – Dec 2021",
        ),
        EducationEntry(
            school="St. Cloud State University",
            program="Computer Science coursework",
            dates="2017 – 2018",
        ),
    ],
    certifications=[
        Certification(
            name="Certificate of Computer Programming",
            issuer="Southern New Hampshire University",
            date="Jan 2022",
        ),
    ],
)
