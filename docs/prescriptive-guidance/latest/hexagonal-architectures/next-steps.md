---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/next-steps.html
---

# Next steps
<a name="next-steps"></a>
+ Familiarize yourself further with domain-driven design concepts by reading the links collected in the [*Resources*](resources.md) section.
+ If you're implementing a new project, use the project structure template provided in this guide and implement a few features.
+ If you're in the process of implementing an existing project, identify code that can be split between read-only and write-only operations. Abstract read-only code into query services, and place write-only code into command handlers.
+ When your base project structure is in place, write unit tests, establish continuous integration (CI) with test automation, and follow test-driven development (TDD) practices.
