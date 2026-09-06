---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/step-4-create-the-module-metadata.html
---

# Step 4: Create the module metadata
<a name="step-4-create-the-module-metadata"></a>

MCS needs additional metadata about a module that isn’t part of the native CloudFormation template. The module metadata is stored in the CloudFormation template in the [Metadata](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html) section. The metadata is stored with the template and no linkage is necessary with an external file.

The [module metadata schema](module-metadata-schema.md) requires the following additional information specific to MCS:
+ Module type
+ Module name
+ Dependencies on other modules
+ Module revision number
