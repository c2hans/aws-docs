---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/faq.html
---

# FAQ
<a name="faq"></a>

**Q. Why should I use a hexagonal architecture? **

**A. **Hexagonal architecture shifts developers' focus to the domain logic, simplifies test automation, and improves code quality and adaptability. These improvements result in a faster time to market and easier technical and organizational scaling.

**Q. Why should I use domain-driven design? **

**A. **Domain-driven design (DDD) enables you to build software components and constructs by using a common language between business stakeholders and engineers. DDD helps you manage software complexity and is an effective strategy for maintaining software products in the long term.

**Q. Can I practice test-driven development without hexagonal architecture?**

**A. **Yes. Test-driven development (TDD) isn't limited to specific software design patterns. However, hexagonal architecture makes it easier to practice TDD.

**Q. Can I scale my product without hexagonal architecture and domain-driven design?**

**A. **Yes. Technical and organizational product scaling can be achieved with most design patterns. However, hexagonal architecture and DDD make it easier to scale and are more effective for large projects in the long term.

**Q. Which technologies should I use to implement hexagonal architecture?**

**A. **Hexagonal architecture isn't limited to a specific technology stack. We recommend that you choose technology that supports dependency inversion and unit testing.

**Q. I am developing a minimum viable product. Does it make sense to spend time thinking about software architecture? **

**A. **Yes. We recommend that you use design patterns that are familiar to you for MVPs. We encourage you to try and practice hexagonal architecture until your engineers are comfortable with it. Establishing a hexagonal architecture for new projects doesn't require a significantly bigger time investment than starting without any architecture.

**Q. I am developing a minimum viable product and have no time to write tests. **

**A. **If your MVP contains business logic, we strongly recommend writing automated tests for it. This will reduce the feedback loop and save time.

**Q. Which additional design patterns can I use with hexagonal architecture? **

**A. **Use the [CQRS pattern](https://www.cosmicpython.com/book/chapter_12_cqrs.html) to support scaling of the overall system. Use the [repository pattern](https://www.cosmicpython.com/book/chapter_02_repository.html) to store and restore your domain model. Use the unit of work pattern to manage transactional process steps. Use composition over inheritance to model domain aggregates, entities, and value objects. Do not build complex object hierarchies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
