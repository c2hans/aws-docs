---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ServiceUpdate.html
---

# ServiceUpdate
<a name="API_ServiceUpdate"></a>

An update that you can apply to your MemoryDB clusters.

## Contents
<a name="API_ServiceUpdate_Contents"></a>

 ** AutoUpdateStartDate **   <a name="MemoryDB-Type-ServiceUpdate-AutoUpdateStartDate"></a>
The date at which the service update will be automatically applied
Type: Timestamp
Required: No

 ** ClusterName **   <a name="MemoryDB-Type-ServiceUpdate-ClusterName"></a>
The name of the cluster to which the service update applies
Type: String
Required: No

 ** Description **   <a name="MemoryDB-Type-ServiceUpdate-Description"></a>
Provides details of the service update
Type: String
Required: No

 ** Engine **   <a name="MemoryDB-Type-ServiceUpdate-Engine"></a>
The name of the engine for which a service update is available.
Type: String
Required: No

 ** NodesUpdated **   <a name="MemoryDB-Type-ServiceUpdate-NodesUpdated"></a>
A list of nodes updated by the service update
Type: String
Required: No

 ** ReleaseDate **   <a name="MemoryDB-Type-ServiceUpdate-ReleaseDate"></a>
The date when the service update is initially available
Type: Timestamp
Required: No

 ** ServiceUpdateName **   <a name="MemoryDB-Type-ServiceUpdate-ServiceUpdateName"></a>
The unique ID of the service update
Type: String
Required: No

 ** Status **   <a name="MemoryDB-Type-ServiceUpdate-Status"></a>
The status of the service update
Type: String
Valid Values: `available | in-progress | complete | scheduled`
Required: No

 ** Type **   <a name="MemoryDB-Type-ServiceUpdate-Type"></a>
Reflects the nature of the service update
Type: String
Valid Values: `security-update`
Required: No

## See Also
<a name="API_ServiceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ServiceUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ServiceUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ServiceUpdate)
