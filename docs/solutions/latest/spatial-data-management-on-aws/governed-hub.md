---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/governed-hub.html
---

# One Governed Record for Spatial Content

Spatial content passes through many tools. A capture is collected in one system, cleaned in another, labeled in a third, used to train a model in a fourth, and the result is checked in another application before it is released. Each hand-off copies files and drops context. Later, it is hard to say which data trained which model, or which version of a scan a result came from.

SDMA is the system of record for that work. It keeps one governed record of each dataset, scene, or capture session, and every result that people rely on comes back to it. Ask of any result: why does it exist, and what made it? The answer comes from the record, not from piecing together logs from five tools.

Work can run in any tool. A result becomes part of the record only when it comes back through SDMA. SDMA records what the result was made from, which connector and settings made it, and who approved the work. The tools around the record, such as processing jobs, models, and partner applications, each read from it, do their work, and write the result back.
+  **More than a data layer.** A bucket or a catalog tells you where files are. SDMA also tells you the current state of an asset, how it was made, and which results can be reused.
+  **More than glue.** Glue copies files from one tool to the next and forgets what happened. A connector is approved configuration, and every run is recorded on the asset it acted on.

Scratch work can live anywhere. Only results that people or other tools rely on need to come back through the record.

| Piece | The problem it solves | What you get |
| --- | --- | --- |
|  **Assets**  | Files in a bucket do not say which belong together, which version is current, or who may open them. | A versioned, permissioned record of the files, metadata, derived content, and history of one dataset, scene, model, or capture session. See [Core Concepts](core-concepts.md). |
|  **Asset templates**  | Every team names, tags, and organizes data differently, so nothing downstream can rely on it. | A contract for a kind of asset: names, required attributes, file types, folder layout, review state, and the connectors allowed to act on it. Every upload is checked against it, so a training job or a script finds what it expects. See [Asset templates](asset-templates.md). |
|  **Connectors**  | Integrations become one-off scripts, each with its own credentials and no record of what ran. | External work declared as configuration, approved per template, and recorded on every run. Results return to the asset as metadata, derived files, and new assets. See [Connectors](connectors.md). |
|  **Viewing**  | You can’t check content you can’t see. Downloading a capture to check it is slow and costly, and it makes copies outside the record. | Point clouds, models, maps, imagery, and video that open in the browser, where the content is stored. Compare two versions, swipe between two images, diff two text files, layer maps, and see what a model found. See [View and inspect your content](view-your-content.md). |
|  **Lineage and provenance**  | A result is only useful if you can say what made it. | Derived files and new assets record what they were made from, which connector version and parameters made them, and which run wrote each attribute value. |

Three rules keep the record whole as you connect more tools to it:
+  **Nothing acts without approval.** A connector does nothing until it is created and approved in a library, a template author approves it for a kind of asset, and a project uses that template. Default connectors need only the library’s approval, because they reach only resources that SDMA deploys: its AWS Deadline Cloud farm and Amazon OpenSearch Serverless. Each level of the chain belongs to a different group of people.
+  **Everything lands in the asset record.** A result is a new version, an attribute, a derived file, or a new asset, with the same permissions and version history as any other change. SDMA writes results nowhere that governance does not cover.
+  **A value from a connector is a claim.** SDMA records which run wrote each value, but it does not vouch for the value. Templates and review states let you decide when a result becomes part of the record that people rely on.

## Runs in Your AWS Account
<a name="governed-hub-in-your-account"></a>

The record is a deployment in your own AWS account, so running it is light:
+  **No servers to manage.** SDMA uses managed AWS services: Amazon Simple Storage Service (Amazon S3), Amazon API Gateway, AWS Lambda, Amazon DynamoDB, and Amazon OpenSearch Serverless. Processing jobs run on AWS Deadline Cloud fleets that scale with demand.
+  **One deployment, not a kit of parts.** Assets, templates, connectors, viewing, search, access control, and lineage come together in one AWS CloudFormation deployment. They share one record, so you do not choose, wire, and upgrade a separate component for each. You launch the stack from the AWS CloudFormation console, with no build tools to install. See [Deploy the Solution](deploy-the-solution.md).
+  **Your content is stored in your account.** Content lives in Amazon S3 in your account, and people and applications come to it. It leaves only through connectors that you approve. Files are stored once by content, so identical files across versions and assets are not duplicated.
+  **Viewing in the browser.** Point clouds, models, maps, imagery, and video open in the Portal, so you do not save a copy of a large capture or install desktop software to check it. See [View and inspect your content](view-your-content.md).
+  **Open to the tools you already use.** Connectors bring models, renderers, and partner applications into the same record by configuration. For example, SDMA works with Veerum, can use VNTANA to transform 3D content, and can integrate with ArcGIS. See [Connectors](connectors.md) and [Partner Integrations](partner-integrations.md).
+  **Costs.** You are responsible for the cost of the AWS services used while running this solution. Some services, such as Amazon OpenSearch Serverless and the VPC endpoints, have a baseline cost even when idle. See [Cost](cost.md).

SDMA is a good fit when your expertise is your content, not application internals. You say what should happen to a kind of asset, such as convert it, run a model on it, or publish it. SDMA starts the work, checks that it is approved, and records the result. You do not write the glue between systems. It fits best when:
+ You manage large spatial or 3D content that several teams and tools touch.
+ You need to show which data produced which result.
+ You want the system to run in your own AWS account without servers to manage.

It is less of a fit when you only need a place to put files and nobody will ask where a result came from.
