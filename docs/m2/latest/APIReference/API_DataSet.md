---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_DataSet.html
---

# DataSet
<a name="API_DataSet"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines a data set.

## Contents
<a name="API_DataSet_Contents"></a>

 ** datasetName **   <a name="m2-Type-DataSet-datasetName"></a>
The logical identifier for a specific data set (in mainframe format).
Type: String
Required: Yes

 ** datasetOrg **   <a name="m2-Type-DataSet-datasetOrg"></a>
The type of dataset. The only supported value is VSAM.
Type: [DatasetOrgAttributes](API_DatasetOrgAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** recordLength **   <a name="m2-Type-DataSet-recordLength"></a>
The length of a record.
Type: [RecordLength](API_RecordLength.md) object
Required: Yes

 ** relativePath **   <a name="m2-Type-DataSet-relativePath"></a>
The relative location of the data set in the database or file system.
Type: String
Required: No

 ** storageType **   <a name="m2-Type-DataSet-storageType"></a>
The storage type of the data set: database or file system. For Micro Focus, database corresponds to datastore and file system corresponds to EFS/FSX. For Blu Age, there is no support of file system and database corresponds to Blusam.
Type: String
Required: No

## See Also
<a name="API_DataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/DataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/DataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/DataSet)
