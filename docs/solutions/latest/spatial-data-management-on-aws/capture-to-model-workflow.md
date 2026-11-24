---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/capture-to-model-workflow.html
---

# Example: From Captured Data to a Deployed Model

Many teams run a loop. They collect data from sensors in the field, turn it into training data, train and validate a model, deploy it, and collect more data. The loop produces large, spatial, versioned content at every step, and the value of the model depends on knowing exactly what it was built from.

SDMA is the record that the loop runs through. The following table shows where each stage of the loop happens, and which SDMA capability supports it.

| Stage | What happens | In SDMA |
| --- | --- | --- |
|  **Capture and ingest**  | Sensors, vehicles, drones, and survey teams produce point clouds, panoramas, video, and logs. | Upload through the Spatial Data Portal, the desktop application, the CLI, or the Amazon S3 import connector. The asset template checks each upload for required attributes such as site, sensor, and capture date, for allowed file types, and for folder layout. An upload that breaks the rules is rejected. |
|  **Enrich**  | Raw captures need previews, standard formats, and searchable metadata. | Content analysis extracts attributes and generates previews. Connectors convert files, for example to a streamable COPC point cloud, and write quality scores and other results back to the asset. See [Connector Patterns for Models and Pipelines](connector-patterns.md). |
|  **Curate and review**  | Teams pick which captures are good enough to train on. | Search by attribute and location. Inspect files in the browser, in place, and compare two versions or several files side by side. A template can hold new assets as drafts until someone reviews them. |
|  **Label and detect**  | Models or people mark what is in the data. | A connector sends files to an inference service, such as an Amazon SageMaker endpoint, and ingests the output as derived files with attributes. The point cloud viewer draws the detections over the scan. |
|  **Train**  | A dataset version becomes a model. | A connector starts a training job, waits for it to finish without holding compute, and registers the trained model as a new asset. The model asset records the dataset and settings that produced it. See [Training a Model and Registering It as an Asset](connector-patterns.md#pattern-train-register). |
|  **Validate**  | You check the model against known cases before it goes out. | Run the model on a held-out asset. The run records the exact model file, the connector version, and the thresholds it used. Open the results in the viewers, and compare versions of a result. |
|  **Deploy and trace**  | The approved model is released, and you can trace it later. | Connectors publish approved assets to the systems that deploy them. For any result, the asset record answers which data, which model, which connector version, and which run. |

Because each stage is a separate connector that reacts to what the previous one wrote, you add a stage, or swap a model, by changing configuration. Nothing is deployed, and the audit trail does not change shape. The **Content flow** tab of an asset template draws the whole chain. See [See How Content Flows Through the Connectors](asset-templates.md#template-content-flow).

The following example shows the **Label and detect** stage. A connector reconstructed the conductors in a power line corridor and measured how close the trees come to them. The point cloud viewer draws the findings over the scan, in a panel titled **Corridor findings**. Each layer in the panel is one kind of finding:
+  **Conductors** – The reconstructed wires, colored by how close the nearest tree comes.
+  **Tree clearance** – Each tree, with a line to the nearest conductor. A slider shows only the trees closer than a distance, and its presets are the clearance zones the run used.
+  **Fall-in risk** – Trees tall enough to strike a conductor if they fall.
+  **Needs review** – Findings where the observed and reconstructed wires disagree.
+  **Utility poles** – The poles that carry a conductor.

For how to read the panel, see [Findings from a Connector Run](view-your-content.md#view-findings).

![Point cloud viewer with a Corridor findings panel on the left and the findings drawn over a scan of a residential area](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/view-findings.png)

 *Point cloud data: Tokyo Metropolitan Government, licensed under CC BY 4.0. For the license terms, see [CC BY 4.0 on the Creative Commons website](https://creativecommons.org/licenses/by/4.0/). Converted for viewing and shown as rendered in the Spatial Data Portal.*

The same pattern fits any workflow where a model’s results inform a person’s decision: inspection programs that flag defects in a scan, mapping teams that classify survey data, and construction teams that compare progress to a plan.
