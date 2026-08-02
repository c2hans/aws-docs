---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources.html
---

# Managing FHIR resources in AWS HealthLake
<a name="managing-fhir-resources"></a>

Use FHIR R4 RESTful API interactions to manage FHIR resources in a HealthLake data store. The following sections describe all HealthLake-supported FHIR R4 RESTful API interactions available for FHIR resource management. For information about HealthLake data store capabilities and which portions of the FHIR specification it supports, see [FHIR R4 Capability Statement for AWS HealthLake](reference-fhir-capability-statement.md).

**Note**
The FHIR interactions listed in this chapter are built in conformance to the HL7 FHIR R4 standard for health care data exchange. Because they are representations of HL7 FHIR services, they are not offered through AWS CLI and AWS SDKs. For more information, see [RESTful API](https://hl7.org/fhir/R4/http.html) in the **FHIR R4 RESTful API documentation**.

The following table lists FHIR R4 interactions supported by AWS HealthLake. For information about FHIR *resource types* supported by HealthLake, see [Resource types](reference-fhir-resource-types.md).

**FHIR R4 interactions supported by AWS HealthLake**
<a name="supported-fhir-interactions"></a>
<table>
<thead>
  <tr><th>Interaction</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2">Whole system interactions</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#capabilities](https://hl7.org/fhir/R4/http.html#capabilities)</td><td>Get a capability statement for the system. See [FHIR R4 Capability Statement for AWS HealthLake](reference-fhir-capability-statement.md).</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#transaction](https://hl7.org/fhir/R4/http.html#transaction)</td><td>Update, create, or delete a set of resources in a single interaction. See [Bundling FHIR resources](managing-fhir-resources-bundle.md).</td></tr>
  <tr><td colspan="2">Type level interactions</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#create](https://hl7.org/fhir/R4/http.html#create)</td><td>Create a new resource with a server-assigned ID. See [Creating a FHIR resource](managing-fhir-resources-create.md).</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#search](https://hl7.org/fhir/R4/http.html#search)</td><td>Search a resource type based on some filter criteria. See [Searching FHIR resources](searching-fhir-resources.md).</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#history](https://hl7.org/fhir/R4/http.html#history)</td><td>Retrieve the change history for a particular resource type. See [Reading FHIR resource history](managing-fhir-resources-read-history.md).</td></tr>
  <tr><td colspan="2">Instance level interactions</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#read](https://hl7.org/fhir/R4/http.html#read)</td><td>Read the current state of a resource. See [Reading a FHIR resource](managing-fhir-resources-read.md).</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#history](https://hl7.org/fhir/R4/http.html#history)</td><td>Read the change history for a particular resource. See [Reading FHIR resource history](managing-fhir-resources-read-history.md).</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#vread](https://hl7.org/fhir/R4/http.html#vread)</td><td>Read the state of a specific version of the resource. See [Reading version-specific FHIR resource history](managing-fhir-resources-read-history.md#managing-fhir-data-get-version-specific-resource).</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#update](https://hl7.org/fhir/R4/http.html#update)</td><td>Update a resource by its ID (or create it if it's new). See [Updating a FHIR resource](managing-fhir-resources-update.md).</td></tr>
  <tr><td>    [https://hl7.org/fhir/R4/http.html#delete](https://hl7.org/fhir/R4/http.html#delete)</td><td>Delete a resource. See [Deleting a FHIR resource](managing-fhir-resources-delete.md).</td></tr>
</tbody>
</table>

**Topics**
+ [Creating a FHIR resource](managing-fhir-resources-create.md)
+ [Reading a FHIR resource](managing-fhir-resources-read.md)
+ [Reading FHIR resource history](managing-fhir-resources-read-history.md)
+ [Updating a FHIR resource](managing-fhir-resources-update.md)
+ [Modifying Resources with PATCH Operation](managing-fhir-resources-patch.md)
+ [Bundling FHIR resources](managing-fhir-resources-bundle.md)
+ [Deleting a FHIR resource](managing-fhir-resources-delete.md)
+ [Idempotency and Concurrency](managing-fhir-resources-idempotency.md)
