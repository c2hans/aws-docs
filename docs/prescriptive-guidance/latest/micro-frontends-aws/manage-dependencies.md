---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/manage-dependencies.html
---

# Managing dependencies for cross-cutting concerns
<a name="manage-dependencies"></a>

Conscious dependency management is important for the success of a distributed architecture such as micro-frontends. It is also a challenging part of micro-frontend development.

In a micro-frontend architecture, two important aspects of dependency management are the performance penalty from transferring large code artifacts to the client, and the overhead on compute resources. Your organization should define how teams maintain dependencies in a distributed frontend architecture.

Three viable strategies for managing dependencies are *share nothing*, *web standards* such as import maps, and *module federation*. Other approaches are generally anti-patterns because they violate basic principles of distributed architectures.

## Share nothing, where possible
<a name="share-nothing"></a>

The share-nothing approach states that independent software artifacts don't share dependencies, or at least don't share them at integration or runtime. This means that if two micro-frontends depend on the same library, each must include the library at build time and ship it separately. Each micro-frontend must also validate that the library doesn't affect global namespaces and shared resources.

This leads to redundancies, but it's a deliberate trade-off that increases agility. Because teams share no runtime dependencies, they have greater flexibility to evolve their software as needed, as long as they stay within the scope of their solution and don't break any interface contracts.

When micro-frontends follow the share-nothing principle, it's important to keep them lightweight. This approach requires developers to optimize their micro-frontends for performance and to avoid sacrificing user experience for developer experience.

## When you share code
<a name="share-code"></a>

When you decide to share code, you can share it as libraries or runtime modules. For example, the frontend core team delivers libraries for micro-frontend consumption through content delivery networks (CDNs). The business value teams can load the libraries at runtime, or they can use package repositories to publish their libraries. Micro-frontend teams can develop against a specific version of the packaged library at build time, similar to mobile applications that use hybrid frameworks.

A third option is to use a private package registry to support build-time integration of common libraries. This reduces the risk that a breaking change in the library contract causes errors at runtime. However, this more conservative approach requires more governance to synchronize all the micro-frontends with newer library versions.

To improve page load times, micro-frontends can externalize the library dependencies to be loaded from cached chunks from a CDN such as Amazon CloudFront.

To manage runtime dependencies, micro-frontends can use import-maps (or libraries such as `System.js`) to specify where each module is loaded from at runtime. webpack Module Federation is another approach to point to a hosted version of a remote module and resolve common dependencies across independent micro-frontends.

Another approach is to facilitate dynamic loading of import-maps with an initial request to a [discovery endpoint](https://github.com/awslabs/frontend-discovery).

## Shared state
<a name="shared-state"></a>

To reduce the coupling of micro-frontends, avoid global state management that is accessible from all the micro-frontends in the same view, similar to monolithic architectures. For example, a global Redux store that is accessible from all micro-frontends increases coupling.

To eliminate shared state, encapsulate it within micro-frontends and communicate by using asynchronous messages, as discussed previously.

When necessary, introduce well-defined interfaces for global state, and opt in to read-only sharing to avoid unexpected behavior:
+ When a vertical split is present, you can use URL components and browser storage to access information from the host environment.
+ When you have a mixed split, you can also use the DOM standard custom events or JavaScript libraries, such as event emitters or bi-directional streams, to pass information to micro-frontends.

If you need to share several pieces of information across micro-frontends, we recommend revisiting the micro-frontend boundaries. Business evolution or an initial design that doesn't meet your needs might cause the need to share.

You can also use server-side sessions, where each micro-frontend fetches the required data by using a session identifier. To reduce coupling, eliminate shared state and keep micro-frontend-specific session data separate.
