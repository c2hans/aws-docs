---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/styling-css.html
---

# Styling and CSS
<a name="styling-css"></a>

Cascading Style Sheets (CSS) is a language for centrally determining the presentation of a document instead of hard-coding formatting for text and objects. The cascading feature of the language controls priorities between styles by using inheritance. When you work on micro-frontends and create a strategy to manage dependencies, the cascading feature can be a challenge.

For example, two micro-frontends coexist on the same page, and each defines its own styling for the `body` HTML element. If each micro-frontend fetches its own CSS file and attaches it to the DOM by using a `style` tag, the second CSS file overrides the first if both files define styles for common HTML elements, class names, or element IDs. You can use different strategies to address these problems, depending on the dependency strategy that you choose for managing styles.

A common approach to balance performance, consistency, and developer experience is to develop and maintain a design system.

## Design systems ‒ A share-something approach
<a name="design-systems"></a>

This approach uses a system to share styling when appropriate while supporting occasional divergence to balance consistency, performance, and developer experience. A design system is a collection of reusable components, guided by clear standards. Design system development is typically driven by one team with input and contributions from many teams. In practical terms, a design system is a way to share low-level elements that can be exported as a JavaScript library. Micro-frontend developers can use the library as a dependency to build simple interfaces by composing premade available resources and as a starting point to make new interfaces.

Consider the example of a micro-frontend that needs a form. The typical developer experience consists of using premade components available in the design system to compose text boxes, buttons, dropdown lists, and other UI elements. The developer doesn't need to write any styling for the actual components, only for how they look together. The system to build and release can use webpack Module Federation or a similar approach to declare the design system as an external dependency, so that the form's logic is packaged without including the design system.

Multiple micro-frontends can then do the same to address shared concerns. When teams develop new components that multiple micro-frontends can share, they add those components to the design system after the components reach maturity.

A main advantage of the design system approach is the high level of consistency. While micro-frontends can write styles and occasionally override those from the design system, there is very little need for that. The main low-level elements don't change often, and they offer basic functionality that is extendable by default. Another advantage is performance. With a good strategy to build and release, you can produce minimal shared bundles that are instrumented by the application shell. You can improve performance even further when micro-frontend-specific bundles are loaded asynchronously on demand, with minimal footprint in terms of network bandwidth. Finally, the developer experience improves because developers can focus on building rich interfaces without recreating common elements (such as writing JavaScript and CSS every time a button needs to be added to a page).

The downside is that a design system of any sort is a dependency, so it must be maintained and sometimes updated. If multiple micro-frontends require a new version of a shared dependency, you can use either of the following:
+ An orchestration mechanism that can occasionally fetch multiple versions of that shared dependency without conflicts
+ A shared strategy to move all the dependents to use a new version

For example, if all micro-frontends depend on version 3.0 of a design system and there is a new version 3.1 that all micro-frontends will share, you can implement feature flags for all micro-frontends to migrate with minimal risk. For more information, see the [Feature flags](feature-flags.md) section. Another potential downside is that design systems usually address more than styling. They also include JavaScript practices and tools. These aspects require reaching consensus through debate and collaboration.

Implementing a design system is a good long-term investment. It's a popular approach, and you should consider it if you work on complex frontend architecture. It typically requires frontend engineers and product and design teams to collaborate and define mechanisms to interact with each other. Schedule time to reach the desired state. Also secure sponsorship from leadership so that people can build something reliable, well-maintained, and performant in the long term.

## Fully encapsulated CSS ‒ A share nothing approach
<a name="encapsulated-css"></a>

Each micro-frontend uses conventions and tools to overcome the cascading feature of CSS. An example is ensuring that each element's style is associated with a class name instead of the element's ID, and that class names are unique. In this way, everything is scoped to individual micro-frontends, which minimizes the risk of unwanted conflicts. The application shell is typically responsible for loading micro-frontends' styles after the micro-frontends load into the Document Object Model (DOM), although some tools bundle the styles together by using JavaScript.

The main advantage of sharing nothing is the reduced risk of introducing conflicts between micro-frontends. Another advantage is an improved developer experience. Because each micro-frontend shares nothing with other micro-frontends, releasing and testing in isolation is simpler and quicker.

A main disadvantage of the share-nothing approach is the potential lack of consistency. This approach has no built-in system to assess consistency. Even if duplicating what's shared is the goal, consistency becomes challenging when you balance speed of release with collaboration. A common mitigation is to create tools to measure consistency. For example, you can create a system that takes automated screenshots of multiple micro-frontends rendered in a page with a headless browser. You can then manually review the screenshots before a release. However, this approach requires discipline and governance. For more information, see the [Balancing autonomy with alignment](balance-autonomy-alignment.md) section.

Depending on the use case, another potential disadvantage is performance. If all the micro-frontends use a large amount of styling, users must download a large amount of duplicated code. This can negatively affect the user experience.

Consider this share-nothing approach only for micro-frontend architectures that involve a few teams, or micro-frontends that can tolerate low consistency. It can also be a natural initial step while an organization works on a design system.

## Shared Global CSS ‒ A share-all approach
<a name="shared-global-css"></a>

With this approach, you store all the code related to styling in a central repository where contributors write CSS for all micro-frontends by working on CSS files or by using preprocessors such as Sass. When contributors change the CSS, a build system creates a single CSS bundle that you can host in a content delivery network (CDN) and that the application shell includes in each micro-frontend. Micro-frontend developers can design and build their applications by running their code through a locally hosted application shell.

In addition to reducing the risk of conflicts between micro-frontends, this approach provides consistency and performance advantages. However, decoupling styles from markup and logic makes it harder for developers to understand how styles are used, how they can evolve, and how they can be deprecated. For example, it might be quicker to introduce a new class name than to learn about the existing class and the consequences of editing its properties. Creating a new class name increases bundle size, which affects performance, and can introduce inconsistencies in the user experience.

While a shared global CSS file can be the starting point of a monolith-to-micro-frontends migration, it's rarely beneficial for micro-frontend architectures in which more than one or two teams collaborate. We recommend that you invest in a design system early and implement a share-nothing approach while you develop the design system.
