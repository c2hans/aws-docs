---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ContainerProductSort.html
---

# ContainerProductSort
<a name="API_ContainerProductSort"></a>

Objects that allows sorting on container products based on certain fields and sorting order.

## Contents
<a name="API_ContainerProductSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SortBy **   <a name="AWSMarketplaceService-Type-ContainerProductSort-SortBy"></a>
Field to sort the container products by.
Type: String
Valid Values: `EntityId | LastModifiedDate | ProductTitle | Visibility | CompatibleAWSServices`
Required: No

 ** SortOrder **   <a name="AWSMarketplaceService-Type-ContainerProductSort-SortOrder"></a>
The sorting order. Can be `ASCENDING` or `DESCENDING`. The default value is `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_ContainerProductSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ContainerProductSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ContainerProductSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ContainerProductSort)
