---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazondynamodbacceleratordax.html
---

# Data retrieval APIs for Amazon DynamoDB Accelerator (DAX)
<a name="amazondynamodbacceleratordax"></a>

Amazon DynamoDB Accelerator (DAX) provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="dax-BatchGetItem"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html) | Return the attributes of one or more items from one or more tables | Read |
| <a name="dax-ConditionCheckItem"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConditionCheckItem.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConditionCheckItem.html) | The ConditionCheckItem operation that checks the existence of a set of attributes for the item with the given primary key | Read |
| <a name="dax-DescribeClusters"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeClusters.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeClusters.html) | Return information about all provisioned DAX clusters | List |
| <a name="dax-DescribeDefaultParameters"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeDefaultParameters.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeDefaultParameters.html) | Return the default system parameter information for DAX | List |
| <a name="dax-DescribeEvents"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeEvents.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeEvents.html) | Return events related to DAX clusters and parameter groups | List |
| <a name="dax-DescribeParameterGroups"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameterGroups.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameterGroups.html) | Return a list of parameter group descriptions | List |
| <a name="dax-DescribeParameters"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameters.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameters.html) | Return the detailed parameter list for a particular parameter group | Read |
| <a name="dax-DescribeSubnetGroups"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeSubnetGroups.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeSubnetGroups.html) | Return a list of subnet group descriptions | List |
| <a name="dax-GetItem"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) | The GetItem operation that returns a set of attributes for the item with the given primary key | Read |
| <a name="dax-ListTags"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ListTags.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ListTags.html) | Return a list all of the tags for a DAX cluster | Read |
| <a name="dax-Query"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) | Use the primary key of a table or a secondary index to directly access items from that table or index | Read |
| <a name="dax-Scan"></a>[https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html) | Return one or more items and item attributes by accessing every item in a table or a secondary index | Read |
