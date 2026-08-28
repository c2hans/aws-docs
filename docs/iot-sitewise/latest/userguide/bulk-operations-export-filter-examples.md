---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/bulk-operations-export-filter-examples.html
---

# Export metadata examples
<a name="bulk-operations-export-filter-examples"></a>

When you perform a bulk export of your AWS IoT SiteWise content to Amazon S3, you can specify *filters* to limit which specific asset models and assets you'd like to export.

You specify the filters in an `iotSiteWiseConfiguration` section within the `sources` section of your request body.

**Note**
You can include multiple filters. The bulk operation will export any asset model or asset that matches any of the filters.
If you don't provide any filters, then the operation will export all of your asset models and assets.

```
{
    "metadataTransferJobId": "{{your-transfer-job-id}}",
    "sources": [{
        "type": "iotsitewise",
        "iotSiteWiseConfiguration": {
            "filters": [{
                {{list of filters}}
            }]
        }
    }],
    "destination": {
        "type": "s3",
        "s3Configuration": {
            "location": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
        }
    }
}
```

## Filter by asset model
<a name="bulk-export-filter-asset-model"></a>

You can filter a specific asset model. You can also include all assets using that model, or all asset models within its hierarchy. You can't include both assets and hierarchy.

For more information about hierarchies, see [Define asset model hierarchies](define-asset-hierarchies.md).

------
#### [ Asset model ]

This filter includes the specified asset model:

```
"filterByAssetModel": {
    "assetModelId": "{{asset model ID}}"
}
```

------
#### [ Asset model and its assets ]

This filter includes the specified asset model, along with all assets using that asset model:

```
"filterByAssetModel": {
    "assetModelId": "{{asset model ID}}",
    "includeAssets": true
}
```

------
#### [ Asset model and its hierarchy ]

This filter includes the specified asset model, along with all associated asset models in its hierarchy:

```
"filterByAssetModel": {
    "assetModelId": "{{asset model ID}}",
    "includeOffspring": true
}
```

------

## Filter by asset
<a name="bulk-export-filter-asset"></a>

You can filter a specific asset. You can also include its asset model, or all associated assets within its hierarchy. You can't include both asset model and hierarchy.

For more information about hierarchies, see [Define asset model hierarchies](define-asset-hierarchies.md).

------
#### [ Asset ]

This filter includes the specified asset:

```
"filterByAsset": {
    "assetId": "{{asset ID}}"
}
```

------
#### [ Asset and its asset model ]

This filter includes the specified asset, along with the asset model it uses:

```
"filterByAsset": {
    "assetId": "{{asset ID}}",
    "includeAssetModel": true
}
```

------
#### [ Asset and its hierarchy ]

This filter includes the specified asset, along with all associated assets in its hierarchy:

```
"filterByAsset": {
    "assetId": "{{asset ID}}",
    "includeOffspring": true
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
