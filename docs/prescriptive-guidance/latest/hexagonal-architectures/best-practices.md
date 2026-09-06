---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/best-practices.html
---

# Best practices
<a name="best-practices"></a>

## Model the business domain
<a name="model-domain"></a>

Work back from the business domain to the software design to ensure that that the software you're writing fits the business need.

Use domain-driven design (DDD) methodologies such as [event storming](https://www.eventstorming.com/) to model the business domain. Event storming has a flexible workshop format. During the workshop, domain and software experts explore the complexity of the business domain collaboratively. Software experts use the deliverables of the workshop to start the design and development process for software components.

## Write and run tests from the beginning
<a name="testing"></a>

Use test-driven development (TDD) to verify the correctness of the software that you are developing. TDD works best at a unit test level. The developer designs a software component by writing a test first, which invokes that component. That component has no implementation at the beginning, therefore the test fails. As a next step, the developer implements the component's functionality, using test fixtures with mock objects to simulate the behavior of external dependencies, or ports. When the test succeeds, the developer can continue by implementing real adapters. This approach improves software quality and results in more readable code, because developers understand how users would use the components. Hexagonal architecture supports the TDD methodology by separating the application core. Developers write unit tests that focus on the domain core behavior. They don't have to write complex adapters to run their tests; instead, they can use simple mock objects and fixtures.

Use behavior-driven development (BDD) to ensure end-to-end acceptance at a feature level. In BDD, developers define scenarios for features and verify them with business stakeholders. BDD tests use as much natural language as possible to achieve this. Hexagonal architecture supports the BDD methodology with its concept of primary and secondary adapters. Developers can create primary and secondary adapters that can run locally without calling external services. They configure the BDD test suite to use the local primary adapter to run the application.

Automatically run each test in the continuous integration pipeline to constantly evaluate the quality of the system.

## Define the behavior of the domain
<a name="behavior"></a>

Decompose the domain into entities, value objects, and aggregates (read about [implementing domain-driven design](https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/)), and define their behavior. Implement the behavior of the domain so that tests that were written at the beginning of the project succeed. Define commands that invoke the behavior of domain objects. Define events that the domain objects emit after they complete a behavior.

Define interfaces that adapters can use to interact with the domain.

## Automate testing and deployment
<a name="automate-testing"></a>

After an initial proof of concept, we recommend that you invest time implementing DevOps practices. For example, continuous integration and continuous delivery (CI/CD) pipelines and dynamic test environments help you maintain the quality of the code and avoid errors during deployment.
+ Run your unit tests inside your CI process and test your code before it is merged.
+ Build a CD process to deploy your application into a static dev/test environment or into dynamically created environments that support automatic integration and end-to-end testing.
+ Automate the deployment process for dedicated environments.

## Scale your product by using microservices and CQRS
<a name="scale"></a>

If your product is successful, scale your product by decomposing your software project into microservices. Utilize the portability that hexagonal architecture provides to improve performance. Split query services and command handlers into separate synchronous and asynchronous APIs. Consider adopting the command query responsibility segregation (CQRS) pattern and event-driven architecture.   If you get many new feature requests, consider scaling your organization based on DDD patterns. Structure your teams in such a way that they own one or more features as bounded contexts, as discussed previously in the [*Organizational scaling*](adapt-to-change.md#scaling) section. These teams can then implement business logic by using hexagonal architecture.

## Design a project structure that maps to hexagonal architecture concepts
<a name="mapping"></a>

Infrastructure as code (IaC) is a widely adopted practice in cloud development. It lets you define and maintain your infrastructure resources (such as networks, load balancers, virtual machines, and gateways) as source code. This way, you can track all changes to your architecture by using a version control system. In addition, you can create and move the infrastructure easily for testing purposes. We recommend that you keep your application code and infrastructure code in the same repository when you develop your cloud applications. This approach makes it easy to maintain infrastructure for your application.

We recommend that you divide your application into three folders or projects that map to the concepts of hexagonal architecture: entrypoints (primary adapters), domain (domain and interfaces), and adapters (secondary adapters).

The following project structure provides an example of this approach when designing an API on AWS. The project maintains application code (app) and infrastructure code (infra) in the same repository, as recommended earlier.

```
app/  # application code
 |--- adapters/  # implementation of the ports defined in the domain
      |--- tests/  # adapter unit tests
 |--- entrypoints/  # primary adapters, entry points
      |--- api/  # api entry point
           |--- model/  # api model
           |--- tests/  # end to end api tests
 |--- domain/  # domain to implement business logic using hexagonal architecture
      |--- command_handlers/  # handlers used to run commands on the domain
      |--- commands/  # commands on the domain
      |--- events/  # events emitted by the domain
      |--- exceptions/  # exceptions defined on the domain
      |--- model/  # domain model
      |--- ports/  # abstractions used for external communication
      |--- tests/  # domain tests
 infra/  # infrastructure code
```

As discussed earlier, the domain is the core of the application and doesn't depend on any other module. We recommend that you structure the domain folder to include the following subfolders:
+ command handlers contains the methods or classes that run commands on the domain.
+ commands contains the command objects that define the information required to perform an operation on the domain.
+ events contains the events that are emitted through the domain and then routed to other microservices.
+ exceptions contains the known errors defined within the domain.
+ model contains the domain entities, value objects, and domain services.
+ ports contains the abstractions through which the domain communicates with databases, APIs, or other external components.
+ tests contains the test methods (such as business logic tests) that are run on the domain.

The primary adapters are the entry points to the application, as represented by the entrypoints folder. This example uses the api folder as the primary adapter. This folder contains an API model, which defines the interface the primary adapter requires to communicate with clients. The tests folder contains end-to-end tests for the API. These are shallow tests that validate that the components of the application are integrated and work in harmony.

The secondary adapters, as represented by the adapters folder, implement the external integrations required by the domain ports. A database repository is a great example of a secondary adapter. When the database system changes, you can write a new adapter by using the implementation that's defined by the domain. There is no need to change the domain or business logic. The tests subfolder contains external integration tests for each adapter.
