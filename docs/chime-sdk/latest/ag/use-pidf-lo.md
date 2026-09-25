---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/use-pidf-lo.html
---

# Using PIDF-LO in emergency calls
<a name="use-pidf-lo"></a>

 Amazon Chime SDK Voice Connectors support enhanced 911 (E911) calling. When you place emergency calls through a Voice Connector, you can send caller location information by including a GEOPRIV Presence Information Data Format Location Object (PIDF-LO) in your SIP requests. The object must include the `Geolocation-Routing` header, set to `Yes`. We strongly recommend [validating the address](validate-emergency-addresses.md). If you don't use addresses or routing numbers, address validation may be carried out at the start of a 911 call to ensure it is routed to the appropriate Public Safety Answering Point (PSAP), meaning help may take longer to arrive.

The following example shows a SIP invite with a PIDF-LO object that includes an address.

```
INVITE sip:911@{{abcdef1ghij2klmno3pqr4}}.voiceconnector.chime.aws;transport=TCP SIP/2.0
Via: SIP/2.0/TCP IPaddress:{{12345}};rport;branch={{z9hG4bKKXN2D41yvDUKH}}
From: {{+15105186683}} ><sip:+15105186683@IPaddress:12345>;tag=tag
To: <sip:911@{{abcdef1ghij2klmno3pqr4}}.voiceconnector.chime.aws>;transport=TCP
Call-ID: {{12abcdef-3456-7891-012g-h7i8j9k6l0a1}}
CSeq: {{43615607}} INVITE
Contact: <sip:{{IPaddress}}:{{12345}}>
Max-Forwards: {{70}}
Geolocation-Routing: {{Yes}}
Geolocation: <cid:{{pidftest@test.com}}>;inserted-by=vpc@ng911.test.com
Content-Type: multipart/mixed;boundary=unique-boundarystring
Content-Length: 271
Accept: application/sdp, application/pidf+xml

--unique-boundarystring
Content-Type: application/sdp
v=0
o=FreeSWITCH {{1636327400}} {{1636327401}} IN IP4 IPaddress
s=FreeSWITCH
c=IN IP4 IPaddress
t=0 0
m=audio 11398 RTP/SAVP 9 0 101
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=sendrecv
a=ptime:20

--unique-boundarystring
Content-Type: application/pidf+xml
Content-ID: <{{pidftest@test.com}}>
<?xml version="1.0" encoding="utf-8"?>
<presence xmlns="urn:ietf:params:xml:ns:pidf"
xmlns:gp="urn:ietf:params:xml:ns:pidf:geopriv10"
xmlns:bp="urn:ietf:params:xml:ns:pidf:geopriv10:basicPolicy"
xmlns:ca="urn:ietf:params:xml:ns:pidf:geopriv10:civicAddr"
entity="sip:{{amazontest911@test.com}}">
<tuple id="0">
    <status>
    <gp:geopriv>
        <gp:location-info>
        <ca:civicAddress>
            <ca:country>US</ca:country>
            <ca:A1>{{WA}}</ca:A1>
            <ca:A3>{{Seattle}}</ca:A3>
            <ca:HNO>{{1812}}</ca:HNO>
            <ca:RD>{{Example}}</ca:RD>
            <ca:STS>Ave</ca:STS>
            <ca:NAM>{{Low Flying Turtle}}</ca:NAM>
            <ca:PC>{{98101}}</ca:PC>
        </ca:civicAddress>
        </gp:location-info>
    </gp:geopriv>
    </status>
    <timestamp>{{2021-09-22T13:37:31.03}}</timestamp>
</tuple>
</presence>
--unique-boundarystring--
```
