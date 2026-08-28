---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/semiconductor-design-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Semiconductor design overview
<a name="semiconductor-design-overview"></a>

Semiconductor design workloads comprise workflows and a supporting set of software tools that enable the efficient design of microelectronics, and in particular, semiconductor ICs. Semiconductor design and verification relies on a set of commercial or open-source tools, collectively referred to as EDA software, which expedites and reduces time to silicon tape-out and fabrication. EDA is a highly iterative engineering process that can take months, and in some cases years, to produce a single integrated circuit.

The increasing complexity of integrated circuits has resulted in an increased use of preconfigured or semi-customized hardware components, collectively known as IP cores. These cores (provided by IP developers as generic gate-level netlists) are either designed in-house by a semiconductor company, or purchased from a third-party IP vendor. IP cores themselves require EDA workflows for design and verification, and to characterize performance for specific IC fabrication technologies. These IP cores are used in combination with IC-specific, custom-designed components, to create a complete IC that often includes a complex system-on-chip (SoC), making use of one of more embedded CPUs, standard peripherals, input/output (I/O), and custom analog and/or digital components.

The complete IC itself, with all its IP cores and custom components, then requires large amounts of processing for full-chip verification, including modeling (simulating) all the components within the chip. This modeling, which includes hardware description language (HDL) source-level validation, physical synthesis, and initial verification (for example, using techniques such as formal verification), is known as the *front-end design*.

The physical implementation, which includes floor planning, place and route, timing analysis, design-rule-check (DRC), and final verification, is known as the *back-end design*. When the back-end design is complete, a file is produced in GDSII format. The production of this file is known as *tape-out*. When completed, the file is sent to a fabrication facility (called a *foundry*), which may or may not be operated by the semiconductor company, where a silicon wafer is manufactured. This wafer, containing perhaps thousands of individual ICs, is then inspected, cut into dies that are themselves tested, packaged into chips that are tested again, and assembled onto a board or other system through highly automated manufacturing processes.

All of these steps in the semiconductor and electronics supply chain can benefit from the scalability of the cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
