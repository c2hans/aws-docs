---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-creation-defaults.html
---

# Client creation defaults
<a name="client-creation-defaults"></a>

In version 2.x, the following changes have been made to the default client creation logic.
+ The default credential provider chain for S3 no longer includes anonymous credentials. You must manually specify anonymous access to S3 by using the `AnonymousCredentialsProvider`.
+ The following environment variables related to default client creation are different.

<table>
<thead>
  <tr><th>1.x</th><th>2.x</th></tr>
</thead>
<tbody>
  <tr><td> <code>AWS_CBOR_DISABLED</code> </td><td> <code>CBOR_ENABLED</code> </td></tr>
  <tr><td> <code>AWS_ION_BINARY_DISABLE</code> </td><td> <code>BINARY_ION_ENABLED</code> </td></tr>
</tbody>
</table>

+ The following system properties related to default client creation are different.

<table>
<thead>
  <tr><th>1.x</th><th>2.x</th></tr>
</thead>
<tbody>
  <tr><td> <code>com.amazonaws.sdk.disableEc2Metadata</code> </td><td> <code>aws.disableEc2Metadata</code> </td></tr>
  <tr><td> <code>com.amazonaws.sdk.ec2MetadataServiceEndpointOverride</code> </td><td> <code>aws.ec2MetadataServiceEndpoint</code> </td></tr>
  <tr><td> <code>com.amazonaws.sdk.disableCbor</code> </td><td> <code>aws.cborEnabled</code> </td></tr>
  <tr><td> <code>com.amazonaws.sdk.disableIonBinary</code> </td><td> <code>aws.binaryIonEnabled</code> </td></tr>
</tbody>
</table>

+ Version 2.x does not support the following system properties.
+

<table>
<thead>
  <tr><th>1.x</th></tr>
</thead>
<tbody>
  <tr><td> <code>com.amazonaws.sdk.disableCertChecking</code> </td></tr>
  <tr><td> <code>com.amazonaws.sdk.enableDefaultMetrics</code> </td></tr>
  <tr><td> <code>com.amazonaws.sdk.enableThrottledRetry</code> </td></tr>
  <tr><td> <code>com.amazonaws.regions.RegionUtils.fileOverride</code> </td></tr>
  <tr><td> <code>com.amazonaws.regions.RegionUtils.disableRemote</code> </td></tr>
  <tr><td> <code>com.amazonaws.services.s3.disableImplicitGlobalClients</code> </td></tr>
  <tr><td> <code>com.amazonaws.sdk.enableInRegionOptimizedMode</code> </td></tr>
</tbody>
</table>

+ Loading Region configuration from a custom `endpoints.json` file is no longer supported.
