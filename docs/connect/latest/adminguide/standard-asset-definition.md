---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/standard-asset-definition.html
---

# Standard asset definition in Connect Customer Customer Profiles
<a name="standard-asset-definition"></a>

The following table lists all the fields in the Customer Profiles standard asset object.

| Standard asset field | Data type | Description |
| --- | --- | --- |
| AssetId | String | The unique identifier of a standard asset. |
| AssetName | String | The asset's name. |
| SerialNumber | String | The asset's serial number. |
| ModelNumber | String | The asset's model number. |
| ModelName | String | The asset's model name. |
| ProductSKU | String | The asset's stock keeping unit. |
| PurchaseDate | String | The asset's purchase date. |
| UsageEndDate | String | The asset's usage end date. |
| Status | String | The asset's status. |
| Price | String | The asset's price. |
| Quantity | String | The asset's quantity. |
| Description | String | The asset's description. |
| AdditionalInformation | String | Any additional information relevant to the asset. |
| DataSource | String | The asset's data source. |
| Attributes | String-to-string map | Key-value pair of attributes of a standard asset. |

The standard asset objects are indexed by the keys in the following table.

| Standard index name | Standard asset field |
| --- | --- |
| \_assetId | AssetId |
| \_assetName | AssetName |
| \_serialNumber | SerialNumber |

For example, you can use `_assetName` as a key name with the [SearchProfiles API](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) to find a profile that has an asset whose AssetName matches with the search value. You can find the standard asset objects associated with a specific profile by using the [ListProfileObjects API](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjects.html) with the `ProfileId` and `ObjectTypeName` set to `_asset`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
