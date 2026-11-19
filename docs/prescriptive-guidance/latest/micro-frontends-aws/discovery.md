---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/discovery.html
---

# Service discovery

The frontend discovery pattern improves the development experience when you develop, test, and deliver micro-frontends. The pattern uses a shareable configuration that describes the entry point of micro-frontends. The shareable configuration also includes additional metadata that supports safe deployments in each environment through canary releases.

Modern frontend development entails using a wide variety of tools and libraries to support modularity during development. Traditionally, this process consisted of bundling code into individual files that you could host in a content delivery network (CDN) to minimize network calls during runtime, including initial load (when an app opens in a browser) and usage (when a customer performs actions such as choosing buttons or inserting information).

## Splitting bundles
<a name="split-bundles"></a>

Micro-frontend architectures help address the performance issues caused by large bundles that result from bundling a large set of functionalities together. For example, you can bundle a large e-commerce website into a 6 MB JavaScript file. Despite compression, the size of that file might negatively affect the user's experience when the app loads and downloads the file from an edge-optimized content delivery network (CDN).

If you split the app into home page, product details, and cart micro-frontends, you can use a bundling mechanism to produce three individual 2 MB bundles. This change might improve first-load performance by up to 300 percent when users load the home page. The app loads the product details and cart micro-frontend bundles asynchronously, only if and when the user visits the product page for an item and decides to purchase it.

Many frameworks and libraries use this approach, and it provides advantages for both customers and developers. To identify business boundaries that can decouple code dependencies, you can map different business functions to multiple teams. Distributed ownership introduces independence and agility.

When you split build packages, you can use a configuration to map micro-frontends and drive the orchestration for the initial load and for post-load navigation. Then, the app can use the configuration during runtime rather than during build time. For example, the client-side frontend code or server-side backend code can make an initial network call to an API to dynamically fetch the list of micro-frontends. The call also fetches the metadata that composition and integration require. You can configure failover strategies and caching for reliability and performance. Mapping the micro-frontends makes individual micro-frontend deployments discoverable by previously deployed micro-frontends that a shell app orchestrates.

## Canary releases
<a name="canary-release"></a>

A canary release is a well-established pattern for deploying microservices. Canary releases divide the target users of a release into multiple groups and release changes gradually, instead of replacing the existing version all at once (as in a blue/green deployment). For example, a canary release strategy might roll out a change to 10 percent of the target users and add 10 percent every minute, so that the release reaches 100 percent of users after 10 minutes.

The goal of a canary release is to get early feedback about changes and reduce the impact of any issues by monitoring the system. When you implement automation, a monitoring system can track business or system metrics and stop the deployment or start a rollback.

For example, a change might introduce a bug that causes a loss of revenue or performance degradation in the first few minutes of a release. Automated monitoring can initiate an alarm. With the service discovery pattern, that alarm can stop the deployment and start a rollback, so the issue affects only 20 percent of users instead of 100 percent. The reduced scope of the issue limits the impact on your business.

For an example architecture that uses DynamoDB as storage to implement a REST Admin API, see the [Frontend Service Discovery on AWS solution](https://github.com/awslabs/frontend-discovery-service) on GitHub. Use the AWS CloudFormation template to integrate the architecture in your own CI/CD pipelines. The solution includes a REST Consumer API for integrating the solution with your frontend applications.
