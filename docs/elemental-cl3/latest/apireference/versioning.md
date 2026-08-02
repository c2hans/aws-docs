---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/versioning.html
---

# Versioning
<a name="versioning"></a>

**Compatibility between XML and Conductor Live Client**
Starting with version 3.0.3, Conductor Live can accept XML that was generated using a software release that is up to 2 versions older.

When submitting a request, specify the version of the XML in the header of the request; see above. When the version is included, the contents of the XML is checked:
+ If there are elements that are required in the current version of the client and they are not in the XML, the client adds them and assigns the default value.
+ If there are elements that are not understood by the current version of Conductor Live, AWS Elemental Live, or AWS Elemental Statmux, the request is rejected.

**Compatibility between Conductor Live and AWS Elemental Live/Statmux**
Each Conductor Live version is compatible with a specific range of AWS Elemental Live or AWS Elemental Statmux versions. For example, an AWS Conductor Live version 3.6.x is compatible with AWS Elemental Live API version 2.13.x for any x.
