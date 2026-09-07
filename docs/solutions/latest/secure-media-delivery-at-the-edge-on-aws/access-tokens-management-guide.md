---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/access-tokens-management-guide.html
---

# Access tokens management guide
<a name="access-tokens-management-guide"></a>

## Varying token attributes
<a name="varying-token-attributes"></a>

 When the access token is created upon viewer request, its final structure is defined by the claims encapsulated in the token. This allows you to vary the parameters used in the token depending on the requested content or viewer type. This is possible because the structure of the token is not fixed and each token can carry a varying set of attributes. Token validation logic implemented in CloudFront Functions has been designed for that as from the set of claims included in JWT token this validation logic at the edge will derive how to correctly process its payload. This quality can be helpful as you can set different tiers of token restrictiveness reflected in used set of attributes for each tier, for example:
+  For viewers originating from countries with a wide geographical range, include region attribute (**reg**) on top of country (**co**) to reduce the risk of unauthorized reuse of the token
+  When a playback session is initiated from the connected TV type of client, you can issue the token based on the viewer’s IP address (**ip**) as it is unlikely it would change throughout the session
+  If the player is capable of generating and repeating a unique session identifier as a custom header, include that header and its value in the viewer attribute and token policy objects
+  For the most premium video assets add more headers in the token policy definition (user-agent, referer etc.) to make it more restrictive

 The list of parameters that can be inserted in the token policy with description can be found in the NodeJS library reference.

 By setting token parameters in a dynamic manner, you can better align the scope of the token for various viewer groups and assets type. In the API module of this solution, and you can test that ability by specifying separate token policies for each video asset inserted in the **[Stack Name]-ApiDemoTable**.

## Choosing session duration time
<a name="choosing-session-duration-time"></a>

 This solution works on the principle that entire playback session is protected by the use of a single token generated only once by the playback API when the playback URL with a token is passed to the player. The issued token is then repeated by the player and therefore it eliminates the need to recompute and refresh the token for the duration of the stream watched. However, when a viewer watches the stream, because the same token is used from the beginning until the end of the playback, it is important to set a correct expiry time to match the expected content duration when known, or a maximum period of time the viewer is expected to watch the same stream continuously (without switching to other channels or video assets). In the case of a stream scheduled with a specific start and end time, you can reflect these time boundaries in **nbf** and **exp** attributes in the token policy using precise timestamps values. For the continuous video streaming channels, when a viewer can start and stop watching the stream at any time, we recommend setting a reasonably high relative time reference in **exp** attribute which reflects typical audience behaviors for how long an uninterrupted, single streaming session can last. For instance, \+4h would issue a token that allows a 4 hours watch time. When a viewer goes past the expiry timestamp after 4 hours, further attempts to use the same token will fail and the client’s application must refresh the stream by requesting a new token from the playback API.

## Using viewer’s source IP in the token
<a name="using-viewers-source-ip-in-the-token"></a>

 A viewer’s source IP can be a very effective mean to reduce the scope of the token and tie it specifically to a single user, eliminating the risk of re-sharing the same playback URL link with the token. While using viewer IP as an input to produce the token gives very strong session uniqueness characteristics of the token, it is also prone to well-known problems that can interrupt a legitimate playback session. This is because a viewer’s IP is not always persistent during the entire time of watching a video content. For example:
+  When a mobile client is switching networks, the source IP changes
+  Some clients are behind gateways or NATs which translate internal client’s address into one of the many potential public addresses available in the pool. While a public IP assigned to the client for any new established connection stays the same for the same TCP session established, the problem arises when the public IP used when communicating with CloudFront distribution differs from the IP address that was used when contacting the playback API. That creates a mismatch between the IP used for generating the token and the IP used when interacting with CloudFront, as shown in the following diagram.

![Diagram of source IP in the token.](https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image20.png)

 To avoid situations in which token validation fails due to a viewer’s IP transitions, use viewer IP with caution when issuing the tokens. We recommend that you use viewer IP only when you have a high level of confidence that the public IP used by the viewer is stable over time, for instance you can set **ip** claim to true (informing the token generate method to use viewer’s IP) when you are able to confirm that client’s device is a connected TV and if you assess that probability of IP change is low. CloudFront can facilitate making this type of decisions with [CloudFront generated headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-cloudfront-headers.html) which specify viewer’s device category.

## Using geo restriction attributes
<a name="using-geo-restriction-attributes"></a>

 One of the categories of available token attributes is related to the geolocation of the viewer, which is verified by the token validator function at the edge. At the token generation stage, you can specify country and region attributes in viewer context object and set the corresponding flags **co** and **reg** to true in the token policy to factor in both when creating the token. Only the viewers whose source IP address is mapped to the same country and region by CloudFront would be permitted provided other matching conditions are also met. The viewer’s country and region are determined by CloudFront and that information is exposed to CloudFront Function through [CloudFront generated headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-cloudfront-headers.html).

 Bear in mind that CloudFront is able to map viewer’s IP address to the geographic location details through an integration with a third-party database as [explained in the documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html). If you are using your own geolocation database with a playback API to determine viewer’s location, it is possible that for certain IP addresses, viewer’s location details are not the same between these the two database sources. This misalignment can in turn result in blocking a legitimate viewer request if geolocation attributes are part of the token. To remove this effect, we recommend that you also retrieve viewer’s geolocation mapping from CloudFront geolocation headers in the playback API request flow. By doing so, you use the same geolocation databases at the stage of producing the token and validating it. To obtain the geolocation information sourced from CloudFront in your playback API, you must set up a CloudFront distribution in front of your API endpoint and make the clients send the requests towards your API through CloudFront distribution, rather than sending request directly to your endpoint. In the configuration of CloudFront distribution facing API endpoint, create and attach the origin request policy to the corresponding cache behavior that includes CloudFront-Viewer-Country and CloudFront-Viewer-Country-Region as the headers to be forwarded to origin. The requests forwarded through CloudFront will contain viewer's geolocation details in these two headers that an API can parse and insert into the viewer attributes object. This design has been implemented in the solution’s API module where API requests are made through CloudFront distribution which supplies upstream API endpoint with geo headers that can be used when creating the token.

![Diagram of geo restriction attributes .](https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image21.png)

 In rare cases, CloudFront might not be able to determine viewer’s location, therefore corresponding geolocation headers will not be present. If the geo restriction attributes **co** or **reg** were added to the token, there are respective fallback claims – **co\_fallback** and **reg\_fallback** flags in the token policy that will also be signalled in the resulting token payload. When set to true, these flags instruct the token validator function to skip the verification step of the viewers’ attributes if viewer location cannot be concluded from the geolocation headers. In that case, the token validation process ignores viewer attributes which includes headers, querystring parameters, session ID, source IP and geolocation attributes, as all of them are verified in a single step. However, JWT token integrity is still validated as well as other attributes as detailed in the token, that is URL path match, expiry time, and nbf timestamp.

## Defining paths list
<a name="defining-paths-list"></a>

 One of the key and mandatory input parameters that must be set in the token policy is a list including path prefixes that the single output token will be covered during the playback session. Each path item in that list can be considered as having implicit, trailing wildcard. That means that if following path item is added in the path’s property:
+  `/video/1/`

   You can use the token for all the assets sharing that path structure, therefore if all the objects required for the playback are available in this directory or its subdirectories, this single path would be enough to restrict the token to that asset and provide uninterrupted playback. All the following requests which come with the token including that path will match this pattern:
+  `/video/1/index.m3u8`
+  `/video/1/uhd/index1.m3u8`
+  `/video/1/index1_02.ts`

   There are some cases however when URL path for the consecutive video objects vary to a high degree where it is impossible to formulate a single path prefix that would scope down the token to a single video asset while covering all the varying URL paths requested during playback. Example of this type of video workload could be AWS Elemental MediaTailor backed workflow, where Elemental MediaTailor becomes a proxy for manifest requests and abstracts directory structure relative to the original path of the manifest. At the same time, URL paths for the original video segment objects remains unchanged and additional ad segments objects are inserted into manifest with their own path patterns. As a result, in a single playback session with MediaTailor in place, you can identify URL paths similar to the following:
+  `/v1/master/1234abcd/Video-HLS/index.m3u8` > master manifest
+  `/v1/manifest/1234abcd/Video-HLS /xwyz-987654321/2.m3u8` > child manifest
+  `/v1/segment/1234abcd/Video-HLS/xwyz-987654321/4/11223355` > ad tracking endpoint
+  `/out/v1/df123456789/index_2_23456.ts?m=1646863308`
+  `/tm/1234abcd/bebgiqk6y5etzpgwfswp6jqccyu7c7ve/asset_720_4_4_00007.ts`

   Assuming all these objects are delivered through CloudFront distribution, to construct a single token that would match all these URL paths patterns but not be over permissive in terms of giving access to more than one video asset it was produced for, craft **path** parameter in the token policy object in a following way:

```
{
  ...

  "paths": [
    "/v1/master/1234abcd/Video-HLS/",
    "/v1/manifest/1234abcd/Video-HLS/",
    "/v1/segment/1234abcd/Video-HLS/",
    "/out/v1/df123456789/",
    "/tm/1234abcd"
  ],
   ...
}
```
