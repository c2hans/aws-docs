---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-cloudfront-presigning.html
---

# Changes in Amazon CloudFront presigning from version 1 to version 2
<a name="migration-cloudfront-presigning"></a>

This topic details the changes in the Amazon CloudFront from version 1 (v1) to version 2 (v2).

## High-level changes
<a name="migration-cloudfront-presigning-api-changes"></a>

****

| Change | v1 | v2 |
| --- | --- | --- |
|  <br />Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.5871}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency>  <br />        <groupId>com.amazonaws</groupId><br />        <artifactId>cloudfront</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.27.212}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>cloudfront</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name | com.amazonaws.services.cloudfront | software.amazon.awssdk.services.cloudfront |
| Class names | [CloudFrontUrlSigner](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloudfront/CloudFrontUrlSigner.html)<br />[CloudFrontCookieSigner](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloudfront/CloudFrontCookieSigner.html) | [CloudFrontUtilities](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudfront/CloudFrontUtilities.html)<br />[SignedUrl](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudfront/url/SignedUrl.html)<br />[CannedSignerRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudfront/model/CannedSignerRequest.html)<br />[CustomSignerRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudfront/model/CustomSignerRequest.html) |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

## API changes
<a name="migration-cf-presign-behavior-changes"></a>

| Behavior | v1 | v2 |
| --- | --- | --- |
| Build a canned request | Arguments are passed directly to the API. |  <pre>CannedSignerRequest cannedRequest =<br />      CannedSignerRequest.builder()<br />                         .resourceUrl(resourceUrl)<br />                         .privateKey(privateKey)<br />                         .keyPairId(keyPairId)<br />                         .expirationDate(expirationDate)<br />                         .build();</pre>  |
| Build a custom request | Arguments are passed directly to the API. |  <pre>CustomSignerRequest customRequest =<br />      CustomSignerRequest.builder()<br />                         .resourceUrl(resourceUrl)<br />                         .resourceUrlPattern(resourceUrlPattern)<br />                         .privateKey(keyFile)<br />                         .keyPairId(keyPairId)<br />                         .expirationDate(expirationDate)<br />                         .activeDate(activeDate)<br />                         .ipRange(ipRange)<br />                         .build();</pre>  |
| Generate a signed URL (canned) |  <pre>String signedUrl =<br />  CloudFrontUrlSigner.getSignedURLWithCannedPolicy(<br />    resourceUrl, keyPairId, privateKey, expirationDate);</pre>  |  <pre>CloudFrontUtilities cloudFrontUtilities =<br />    CloudFrontUtilities.create();<br /><br />SignedUrl signedUrl =        <br />    cloudFrontUtilities.getSignedUrlWithCannedPolicy(cannedRequest);<br /><br />String url = signedUrl.url();<br /></pre>  |
| Generate a signed cookie (custom) |  <pre>CookiesForCustomPolicy cookies =<br />    CloudFrontCookieSigner.getCookiesForCustomPolicy(<br />        resourceUrl, privateKey, keyPairId, expirationDate, <br />        activeDate, ipRange);<br /></pre>  |  <pre>CloudFrontUtilities cloudFrontUtilities =<br />    CloudFrontUtilities.create();<br /><br />CookiesForCustomPolicy cookies =<br />     cloudFrontUtilities.getCookiesForCustomPolicy(customRequest);<br /></pre>  |

### Refactored cookie headers in v2
<a name="migration-cf-presign-behavior-headers"></a>

In Java v1, the Java SDK delivers cookie headers as a `Map.Entry<String, String>`.

```
Map.Entry<String, String> signatureMap = cookies.getSignature();
String signatureKey = signatureMap.getKey(); // "CloudFront-Signature"
String signatureValue = signatureMap.getValue(); // "[SIGNATURE_VALUE]"
```

The Java v2 SDK delivers the entire header as a single `String`.

```
String signatureHeaderValue = cookies.signatureHeaderValue(); // "CloudFront-Signature=[SIGNATURE_VALUE]"
```
