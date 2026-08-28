---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/frameworks-tools.html
---

# Frameworks and tools
<a name="frameworks-tools"></a>

There is no shortage of frontend frameworks, such as Angular and Next.js, but most of them are not created with micro-frontends in mind. Therefore, they are sometimes missing mechanisms to address the challenges of micro-frontend architecture.

## General framework considerations
<a name="framework-general"></a>

This guide doesn't aim to recommend, or to compare, individual frameworks. As multiple micro-frontends often run on the same web application page, loading and runtime performance are major concerns. It's important to choose a framework that introduces as little overhead as possible.

Frameworks are divided based on the rendering layer:
+ Client-side rendering (CSR)
+ Server-side rendering (SSR)

Frontend architectures include other capabilities, such as static site generation (SSG). However, SSG is performed one time only. Micro-frontends are mainly composed at runtime, so CSR and SSR are the main options.

### Client-side rendering
<a name="client-side-rendering.4b55fc6d-c883-50b3-899b-024d6e111700"></a>

For CSR, there are two popular options:
+ Single SPA framework
+ Module Federation

Single SPA is a lightweight choice for composing micro-frontends. It solves the most common challenges in micro-frontend architectures, such as composing multiple micro-frontends in the same page and avoiding dependency clashes.

Module Federation started as a plugin, offered by webpack 5, and it solves a vast majority of the challenges in micro-frontend architectures, including dependencies management across different artifacts. Module Federation 2.0 works natively with Rspack, webpack, esbuild, and now with JavaScript.

Consider not using a framework at all. Modern browsers, with a market share of 98 percent overall according to [caniuse.com](https://caniuse.com/usage-table), offer features such as custom elements natively, and they are adequate for a micro-frontends application. Where necessary, combine custom elements with lightweight libraries for event propagation, internationalization, or other specific concerns.

### Server-side rendering
<a name="server-side-rendering.f75bd94f-ecf9-5e55-89b0-3e03b64bf511"></a>

On the SSR side, the two main options are more complicated:
+ Embrace an existing framework such as Next.js, and apply a micro-frontends principle that uses Module Federation.
+ Use HTML-over-the-wire to exchange HTML fragments that represent micro-frontends, and compose these fragments inside a template at runtime. An example of this approach is Podium.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
