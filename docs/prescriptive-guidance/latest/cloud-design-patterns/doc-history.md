---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/doc-history.html
---

# Document history
<a name="doc-history"></a>

The following table describes significant changes to this guide.

|
|
| Change | Description | Date |
| --- |--- |--- |
| New patterns | Added two new patterns: [hexagonal architecture](hexagonal-architecture.md) and [scatter-gather](scatter-gather.md). | May 7, 2024 |
| New code examples | Added sample code for the [change data capture (CDC) use case](transactional-outbox.md#transactional-implementation-code-cdc) to the transactional outbox pattern pattern. | February 23, 2024 |
| New code examples | + Updated the [transactional outbox pattern](transactional-outbox.md) with sample code.<br />+ Removed the section on orchestration and choreography patterns, which were superseded by [saga choreography](saga-choreography.md) and [saga orchestration](saga-orchestration.md). | November 16, 2023 |
| New patterns | Added three new patterns: [saga choreography](saga-choreography.md), [publish-subscribe](publish-subscribe.md), and [event sourcing](event-sourcing-pattern.md). | November 14, 2023 |
| Update | Updated the [strangler fig pattern implementation](strangler-fig.md#strangler-fig-implementation) section. | October 2, 2023 |
| Initial publication | This first release includes eight design patterns: anti-corruption layer (ACL), API routing, circuit breaker, orchestration and choreography, retry with backoff, saga orchestration, strangler fig, and transactional outbox. | July 28, 2023 |
