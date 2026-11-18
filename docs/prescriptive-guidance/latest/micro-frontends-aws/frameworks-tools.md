---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/frameworks-tools.html
---

# Frameworks and tools
<a name="frameworks-tools"></a>

Many frontend frameworks, such as Angular and Next.js, do not design for micro-frontends as a primary use case. As a result, they can lack mechanisms to address the challenges of micro-frontend architecture.

## General framework considerations
<a name="framework-general"></a>

This guide doesn't aim to recommend, or to compare, individual frameworks. As multiple micro-frontends often run on the same web application page, loading and runtime performance are major concerns. It's important to choose a framework that introduces as little overhead as possible.

You can divide frameworks based on the rendering layer:
+ Client-side rendering (CSR)
+ Server-side rendering (SSR)

Frontend architectures include other capabilities, such as static site generation (SSG). However, SSG runs only once. You mainly compose micro-frontends at runtime, so CSR and SSR are the main options.

### Client-side rendering
<a name="client-side-rendering.2cd25415-8705-5f79-bc65-c8e755d23f05"></a>

For CSR, there are two popular options:
+ Single SPA framework
+ Module Federation

Single SPA is a lightweight choice for composing micro-frontends. It solves the most common challenges in micro-frontend architectures, such as composing multiple micro-frontends in the same page and avoiding dependency clashes.

Module Federation started as a plugin offered by webpack 5. It addresses many of the challenges in micro-frontend architectures, including dependency management across different artifacts. Module Federation 2.0 works natively with Rspack, webpack, esbuild, and now with JavaScript.

Consider not using a framework at all. Modern browsers, with a market share of 98 percent overall according to [caniuse.com](https://caniuse.com/usage-table), offer features such as custom elements natively, and they are adequate for a micro-frontends application. Where necessary, combine custom elements with lightweight libraries for event propagation, internationalization, or other specific concerns.

### Server-side rendering
<a name="server-side-rendering.9d9d35ea-4eba-51b2-bb7e-dd4f4a1b152d"></a>

On the SSR side, the two main options are more complicated:
+ Use an existing framework such as Next.js, and apply a micro-frontends principle that uses Module Federation.
+ Use HTML-over-the-wire to exchange HTML fragments that represent micro-frontends, and compose these fragments inside a template at runtime. An example of this approach is Podium.
