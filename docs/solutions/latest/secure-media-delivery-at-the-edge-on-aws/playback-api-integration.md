---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/playback-api-integration.html
---

# Playback API integration
<a name="playback-api-integration"></a>

 The Secure Media Delivery at the Edge on AWS solution provides a reference architecture which encompasses the entire process of managing secure access tokens in the video streaming workload. The primary and universal components of the solution are defined in the base module which governs the functionality of token validation and signing key management. This part of the solution remains unchanged as you implement your solution across your workloads and it is not expected that this part of the workflow, responsible for token validation, would require any customization to watch varying video streaming workloads. On the other hand, the API module is offered as a reference implementation of the initial stage of the end-to-end workflow which entails Playback API service – an endpoint that is responsible for vending the secure tokens to authorized viewers and returning playback URLs to the viewers. This module also comes with a demo website that allows you to test and validate the usage of the solution but it is not meant to use in production environments. As this solution provides incremental security layer to existing video streaming workloads, depending on your current implementation of a Playback API endpoint you can decide the best approach to customize and integrate the elements available in the solution to introduce the token generation function into your existing workflow.

 Before you implement the most preferable integration option, make sure that before using the solution in production you turn off and remove the artifacts that the demo website is built on.
