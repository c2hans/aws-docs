---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/marketplace-catalog_example_marketplace-catalog_PublishExistingSaas_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Publish a SaaS product and associated public offer from an existing draft using an AWS SDK
<a name="marketplace-catalog_example_marketplace-catalog_PublishExistingSaas_section"></a>

The following code example shows how to publish a SaaS product and associated public offer from an existing draft. The product will be in a limited state by default.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#catalog-api-reference-code) repository.

```
{
    "Catalog":"AWSMarketplace",
    "ChangeSet": [
        {
            "ChangeType": "UpdateVisibility",
            "ChangeName": "CreateProductChange",
            "Entity": {
                "Type": "SaaSProduct@1.0",
                "Identifier": "prod-1111111111111"
            },
            "DetailsDocument": {
                "TargetVisibility": "Public"
            }
        }
    ]
}
```
+  For API details, see [StartChangeSet](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/StartChangeSet) in *AWS SDK for Java 2.x API Reference*.

------
