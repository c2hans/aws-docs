---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InferredWorkloadSaving.html
---

# InferredWorkloadSaving
<a name="API_InferredWorkloadSaving"></a>

 The estimated monthly savings after you adjust the configurations of your instances running on the inferred workload types to the recommended configurations. If the `inferredWorkloadTypes` list contains multiple entries, then the savings are the sum of the monthly savings from instances that run the exact combination of the inferred workload types.

## Contents
<a name="API_InferredWorkloadSaving_Contents"></a>

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-InferredWorkloadSaving-estimatedMonthlySavings"></a>
An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing.
Type: [EstimatedMonthlySavings](API_EstimatedMonthlySavings.md) object
Required: No

 ** inferredWorkloadTypes **   <a name="computeoptimizer-Type-InferredWorkloadSaving-inferredWorkloadTypes"></a>
The applications that might be running on the instance as inferred by Compute Optimizer.
Compute Optimizer can infer if one of the following applications might be running on the instance:
+  `AmazonEmr` - Infers that Amazon EMR might be running on the instance.
+  `ApacheCassandra` - Infers that Apache Cassandra might be running on the instance.
+  `ApacheHadoop` - Infers that Apache Hadoop might be running on the instance.
+  `Memcached` - Infers that Memcached might be running on the instance.
+  `NGINX` - Infers that NGINX might be running on the instance.
+  `PostgreSql` - Infers that PostgreSQL might be running on the instance.
+  `Redis` - Infers that Redis might be running on the instance.
+  `Kafka` - Infers that Kafka might be running on the instance.
+  `SQLServer` - Infers that SQLServer might be running on the instance.
Type: Array of strings
Valid Values: `AmazonEmr | ApacheCassandra | ApacheHadoop | Memcached | Nginx | PostgreSql | Redis | Kafka | SQLServer`
Required: No

## See Also
<a name="API_InferredWorkloadSaving_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/InferredWorkloadSaving)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/InferredWorkloadSaving)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/InferredWorkloadSaving)
