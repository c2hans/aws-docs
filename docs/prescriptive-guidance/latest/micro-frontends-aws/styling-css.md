---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/styling-css.html
---

# Styling and CSS
<a name="styling-css"></a>

Cascading Style Sheets (CSS) is a language for centrally determining the presentation of a document instead of hard-coding formatting for text and objects. The cascading feature of the language is designed to control priorities between styles by using inheritance. When you work on micro-frontends and create a strategy to manage dependencies, the cascading feature of the language can be a challenge.

For example, two micro-frontends co-exist on the same page, each defining its own styling for the `body` HTML element. If each fetches its own CSS file and attaches it to the DOM by using a `style` tag, the CSS file overrides the first if they both have definition for common HTML elements, class names or element IDs. There are different strategies to deal with these problems, depending on the dependency strategy that you pick for managing styles.

Currently, the most popular approach to balance performance, consistency, and developer experience consists of developing and maintaining a design system.

## Design systems ‒ A share-something approach
<a name="design-systems"></a>

This approach uses a system to share styling when appropriate while supporting occasional divergence to balance consistency, performance, and developer experience. A design system is a collection of reusable components, guided by clear standards. Design system development is typically driven by one team with input and contributions from many teams. In practical terms, a design system is a way to share low-level elements that can be exported as a JavaScript library. Micro-frontend developers can use the library as a dependency to build simple interfaces by composing premade available resources and as a starting point to make new interfaces.

Consider the example of a micro-frontend that needs a form. The typical developer experience consists of using premade components available in the design system to compose text boxes, buttons, dropdown lists, and other UI elements. The developer doesn't need to write any styling for the actual components, only for how they look together. The system to build and release can use webpack Module Federation or a similar approach to declare the design system as an external dependency, so that the form's logic is packaged without including the design system.

Multiple micro-frontends can then do the same to take care of shared concerns. When teams develop new components that can be shared between multiple micro-frontends, those components are added to the design system after they reach maturity.

A main advantage of the design system approach is the high level of consistency. While micro-frontends can write styles and occasionally override those from the design system, there is very little need for that. The main low-level elements don't change often, and they offer basic functionality that is extendable by default. Another advantage is performance. With a good strategy to build and release, you can produce minimal shared bundles that are instrumented by the application shell. You can improve even further when multiple micro-frontend specific bundles are asynchronously loaded on demand, with minimal footprint in terms of network bandwidth. Last but not least, the developer experience is ideal because people can focus on building rich interfaces without reinventing the wheel (such as writing JavaScript and CSS every time a button needs to be added to a page).

The downside is that a design system of any sort is a dependency, so it must be maintained and sometimes updated. If multiple micro-frontends require a new version of a shared dependency, you can use either of the following:
+ An orchestration mechanism that can occasionally fetching multiple versions of that shared dependency without conflicts
+ A shared strategy to move all the dependents to use a new version

For example, if all micro-frontends depend on the version 3.0 of a design system and there is a new version called 3.1 to be used in a shared manner, you can implement feature flags for all micro-frontends to migrate with minimal risk. For more information, see the [Feature flags](feature-flags.md) section. Another potential downside is that design systems usually address more than styling. They also include JavaScript practices and tools. These aspects require reaching consensus through debate and collaboration.

Implementing a design system is a good long-term investment. It's a popular approach, and it should be considered by anyone working on complex frontend architecture. It typically requires frontend engineers and product and design teams to collaborate and define mechanisms to interact with each other. It's important to schedule time to reach the desired state. It's also important to have sponsorship from the leadership so that people can build something reliable, well-maintained, and performant in the long term.

## Fully encapsulated CSS ‒ A share nothing approach
<a name="encapsulated-css"></a>

Each micro-frontend uses conventions and tools to overcome the cascading feature of CSS. An example is ensuring each element's style is always associated with a class name instead of the element's ID, and class names are always unique. In this way, everything is scoped to individual micro-frontends, and the risk of unwanted conflicts is minimized. The application shell is typically in charge of loading micro-frontends' styles after they are loaded into the DOM, although some tools bundle the styles together by using JavaScript.

The main advantage of sharing nothing is the reduced risk of introducing conflicts between micro-frontends. Another advantage is the developer's experience. Each micro-frontend shares nothing with other micro-frontends. Releasing and testing in isolation is simpler and quicker.

A main disadvantage of the share-nothing approach is the potential lack of consistency. No system is in place to assess consistency. Even if duplicating what's shared is the goal, it becomes challenging when balancing speed of release and collaboration. A common mitigation is to create tools to measure consistency. For example, you can create a system to take automated screenshots of multiple micro-frontends rendered in a page with a headless browser. You can then manually review the screenshots before a release. However, that requires discipline and governance. For more information, see the [Balancing autonomy with alignment](balance-autonomy-alignment.md) section.

Depending on the use case, another potential disadvantage is performance. If a large amount of styling is used by all the micro-frontends, the customer must download a lot of duplicated code. That will negatively affect the user experience.

This share-nothing approach should be considered only for micro-frontend architectures that involve only a few teams, or micro-frontends that can tolerate low consistency. It can also be a natural initial step while an organization is working on a design system.

## Shared Global CSS ‒ A share-all approach
<a name="shared-global-css"></a>

With this approach, all the code related to styling is stored in a central repository where contributors write CSS for all micro-frontends by working on CSS files or by using preprocessors such as Sass. When changes are made, a build system creates a single CSS bundle that can be hosted in a CDN and included in each micro-frontend by the application shell. Micro-frontend developers can design and build their applications by running their code through a locally hosted application shell.

Apart from the obvious advantage of reducing risk of conflicts between micro-frontends, the advantages of this approach are consistency and performance. However, decoupling styles from markup and logic makes it harder for developers to understand how styles are used, how they can evolve, and how they can be deprecated. For example, it might be quicker to introduce a new class name than to learn about the existing class and the consequences of editing its properties. The disadvantages of creating a new class name are bundle-size growth, which affects performance, and the potential introduction of inconsistencies in the user experience.

While a shared global CSS can be the starting point of a monolith-to-micro-frontends migration, it's rarely beneficial for micro-frontend architectures that involve more than one or two teams collaborating together. We recommend investing in a design system as soon as possible and implementing a share-nothing approach while the design system is in development.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
