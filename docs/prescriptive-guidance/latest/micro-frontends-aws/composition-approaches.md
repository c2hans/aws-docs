---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/composition-approaches.html
---

# Composing pages and views with micro-frontends
<a name="composition-approaches"></a>

You can compose views of an application with client-side composition, edge-side composition, and server-side composition. The composition patterns have different characteristics in terms of necessary team skills, fault tolerance, performance, and cache behavior.

The following diagram shows how the composition happens at the client-side, edge-side, and server-side layers of a micro-frontend architecture.

![Origin, CDN, and client having micro-frontends in client-side, edge-side, and server-side layers.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/96be30ad-858f-4fdc-aee1-70f0d03bebfa.png)

The client-side, edge-side and server-side layers are discussed in the following sections.

## Client-side composition
<a name="client-side-composition"></a>

Dynamically load and append micro-frontends as Document Object Model (DOM) fragments on the client (browser or mobile web view). The micro-frontend artifacts, such as JavaScript or CSS files, can be loaded from content delivery networks (CDNs) for reduced latency. Client-side composition requires the following:
+ A team to own and maintain a shell application or a micro-frontend framework to enable discovery, loading, and rendering micro-frontend components at runtime in the browser
+ High skill levels in front-end technologies such as HTML, CSS, and JavaScript, and in-depth understanding of browser environments
+ Optimization of the amount of JavaScript loaded in a page, and discipline to avoid global namespace clashes

The following diagram shows an example AWS architecture for serverless client-side composition.

![Web app connects through CloudFront to the micro-frontend discovery service and Amazon S3.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/9e5ef5c8-08cb-4f9f-a890-904399100237.png)

Client-side composition happens in the browser environment through a shell application. The diagram shows the following details:

1. After the shell application is loaded, it makes an initial request to [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) to discover the micro-frontends to be loaded through a manifest endpoint.

1. Manifests contain information about each micro-frontend (for example, name, URL, version, and fallback behavior). The manifests are served by the micro-frontends discovery service. In the diagram, this discovery service is represented by Amazon API Gateway, an AWS Lambda function, and Amazon DynamoDB. The shell application uses the manifest information to request individual micro-frontends to compose the page within a given layout.

1. Each micro-frontend bundle is composed of static files (such as JavaScript, CSS, and HTML). The files are hosted in an [Amazon Simple Storage Service (Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)) bucket and served through CloudFront.

1. Teams can deploy new versions of their micro-frontends and update the manifest information by using deployment pipelines that they own.

## Edge-side composition
<a name="edge-side-composition"></a>

Use transclusion techniques such as Edge Side Includes (ESI) or Server Side Includes (SSI) supported by some CDNs and proxies in front of origin servers to compose a page before sending it over the wire to the clients. ESI requires the following:
+ A CDN with ESI capability, or a proxy deployment in front of server-side micro-frontends. Proxy implementations such as HAProxy, Varnish, and NGINX support SSI.
+ An understanding of the use and limitations of ESI and SSI implementations.

Teams starting new applications typically don't choose edge-side composition for their composition pattern. However, this pattern might provide a pathway for legacy applications that rely on transclusion.

## Server-side composition
<a name="server-side-composition"></a>

Use origin servers to compose pages before they are cached on the edge. This can be done with traditional technologies, such as PHP, Jakarta Server Pages (JSP), or templating libraries, to compose the pages by including fragments from micro-frontends. You can also use JavaScript frameworks, such as Next.js, running on the server to compose pages on the server with server-side rendering (SSR).

After the pages are rendered on the server, they can be cached on CDNs to reduce latency. When new versions of micro-frontends are deployed, pages must be re-rendered, and the cache must be updated to deliver the latest versions to customers.

Server-side composition requires an in-depth understanding of the server environment to establish patterns for deployment, discovery of server-side micro-frontends, and cache management.

The following diagram shows server-side composition.

![Server-side composition in seven steps.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/5174e26b-de2c-4681-bb02-f4126b077794.png)

The diagram includes the following components and processes:

1. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) provides a unique entry point to the application. The distribution has two origins: the first for static files and the second for the UI composer.

1. Static files are hosted in an [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket. They are consumed by the browser and the UI composer for HTML templates.

1. The UI composer runs on a containers cluster in [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html). With a containerized solution, you can use streaming capabilities and multithreaded rendering if needed.

1. [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), a capability of AWS Systems Manager, is used as a basic micro-frontends discovery system. This capability provides a key-value store used by the UI composer for retrieving the micro-frontend endpoints to consume.

1. The notifications micro-frontend stores the optimized JavaScript bundle in the S3 bucket. This renders on the client because it must react to user interactions.

1. The reviews micro-frontend is composed by a [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function, and the user reviews are stored in [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html). The reviews micro-frontend is rendered fully on the server side, and it outputs an HTML fragment.

1. The product details micro-frontend is a low-code micro-frontend that uses [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). The Express Workflow can be invoked synchronously, and it contains the logic for rendering the HTML fragment and a caching layer.

For more information about server-side composition, see the blog post [Server-side rendering micro-frontends – the architecture](https://aws.amazon.com/blogs/compute/server-side-rendering-micro-frontends-the-architecture/).
