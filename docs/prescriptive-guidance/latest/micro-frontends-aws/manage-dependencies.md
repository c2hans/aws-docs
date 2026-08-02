---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/manage-dependencies.html
---

# Managing dependencies for cross-cutting concerns
<a name="manage-dependencies"></a>

Conscious dependency management is crucial for the success of a distributed architecture such as micro-frontends. Dependency management is one of the most challenging parts of micro-frontend development.

In a micro-frontend architecture, two important aspects of dependency management are the performance penalty from transferring large code artifacts to the client, and the overhead in compute resources. Ideally, your organization needs to mandate how dependencies in a distributed frontend architecture are maintained.

Three viable strategies for mandating dependency maintenance are *share nothing*, using web standards such as import maps, and *module federation*. Other approaches are anti-patterns because they violate basic principles of distributed architectures.

## Share nothing, where possible
<a name="share-nothing"></a>

The share-nothing approach postulates that no dependencies between independent software artifacts should be shared at all, or at least not at integration or runtime. This means that if two micro-frontends depend on the same library, each must bake in the library at build time and ship it separately. Also, each micro-frontend must validate that the library does not pollute global namespaces and shared resources.

This leads to redundancies, but it is a conscious trade-off with maximum agility. With no runtime dependencies shared, teams have maximum flexibility to evolve the software in any way they see useful as long as they do so in the scope of their solution and don't break any interface contracts.

On a platform where micro-frontends follow the share-nothing principle, it's important to keep micro-frontends as lightweight as possible. It requires developers who are skilled and diligent in optimizing their micro-frontends for performance and who don't sacrifice user experience for developer experience.

## When you share code
<a name="share-code"></a>

When you make the decision to share some code, you can share it as libraries or runtime modules. For example, the frontend core team delivers libraries for micro-frontend consumption through CDNs. The business value teams can load the libraries at runtime, or they can use package repositories to publish their libraries. Micro-frontend teams can develop against a specific version of the packaged library at build time, similar to mobile applications using hybrid frameworks.

A third option is to use a private package registry to support build-time integration of common libraries. This reduces the risk that a breaking change in the library contract initiates errors at runtime. However, this more conservative approach requires more governance in place to synchronize all the micro-frontends with newer library versions.

To improve the page load times, micro-frontends can externalize the library dependencies to be loaded from cached chunks from a CDN such as Amazon CloudFront.

To manage runtime dependencies, micro-frontends can use import-maps (or libraries such as `System.js`) to specify where each module is loaded from at runtime. webpack Module Federation is another approach to point to a hosted version of a remote module and resolve common dependencies across independent micro-frontends.

Another approach is to facilitate dynamic loading of import-maps with an initial request to a [discovery endpoint](https://github.com/awslabs/frontend-discovery).

## Shared state
<a name="shared-state"></a>

To reduce the coupling of micro-frontends, it's important to avoid a global state management accessible from all the micro-frontends in the same view, similar to monolithic architectures. For example, having a global Redux store accessible from all micro-frontends increases coupling.

A pattern to eliminate shared state is to encapsulate it within micro-frontends, and communicate with asynchronous messages as discussed previously.

When absolutely necessary, introduce well-defined interfaces for global state, and opt in for read-only sharing to avoid unexpected behavior:
+ When a vertical split is present, you can use URL components and browser storage to access information from the host environment.
+ When you have a mixed split, you can also use the DOM standard custom events or JavaScript libraries, such as event emitters or bi-directional streams, to pass information to micro-frontends.

If you need to share several pieces of information across micro-frontends, we recommend revisiting the micro-frontend boundaries. The need to share might be caused by business evolution or a subpar initial design.

It's also possible to use server-side sessions, where each micro-frontend fetches the required data by using a session identifier. To reduce coupling, it's important to eliminate shared state and to keep micro-frontend specific session data separate.
