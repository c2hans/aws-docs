---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/web-architecture.html
---

# Understanding web application architecture for the Amazon Chime SDK
<a name="web-architecture"></a>

You can serve your web application from a content delivery network, and load it when the user navigates to a URL in a browser. You can also wrap it in a platform-native Electron application that the user installs on their machine.

To join a new or existing meeting, the web application makes REST requests to the server application. Typically, the requests carry an authorization token or a cookie that your application uses for other API requests. You can also design your web client to send a region hint to the server, which the latter can use when providing the MediaRegion parameter to [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html). Your web application can determine the closest media services region by making an HTTP GET request to the [ https://nearest-media-region.l.chime.aws ](https://nearest-media-region.l.chime.aws/) endpoint.
