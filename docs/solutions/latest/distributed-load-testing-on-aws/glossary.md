---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/glossary.html
---

# Glossary
<a name="glossary"></a>

This glossary defines acronyms and abbreviations used throughout the Distributed Load Testing on AWS Implementation Guide.

## Technical Protocols and Formats
<a name="technical-protocols-and-formats"></a>

AGPL
Affero General Public License. An open-source software license used by k6.

API
Application Programming Interface. A set of protocols and tools for building software applications and enabling communication between different systems.

CLI
Command Line Interface. A text-based interface for interacting with software and operating systems.

CORS
Cross-Origin Resource Sharing. A security feature that allows or restricts web applications running at one origin to access resources from a different origin.

CSV
Comma-Separated Values. A file format used to store tabular data in plain text, commonly used for data export.

gRPC
gRPC Remote Procedure Call. A high-performance, open-source framework for remote procedure calls.

HTTP
Hypertext Transfer Protocol. The foundation protocol used for transmitting data on the World Wide Web.

HTTPS
HTTP Secure. An extension of HTTP that uses encryption for secure communication over a network.

JSON
JavaScript Object Notation. A lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.

JWT
JSON Web Token. A compact, URL-safe means of representing claims to be transferred between two parties for authentication and authorization.

OAuth
Open Authorization. An open standard for access delegation commonly used for token-based authentication and authorization.

REST
Representational State Transfer. An architectural style for designing networked applications using stateless communication and standard HTTP methods.

SSE
Server-Sent Events. A server push technology enabling a client to receive automatic updates from a server via an HTTP connection.

UI
User Interface. The visual elements and controls through which users interact with software applications.

URL
Uniform Resource Locator. The address used to access resources on the internet.

XML
Extensible Markup Language. A markup language that defines rules for encoding documents in a format that is both human-readable and machine-readable.

## Testing and Database Terms
<a name="testing-and-database-terms"></a>

FTP
File Transfer Protocol. A standard network protocol used for transferring files between a client and server.

GSI
Global Secondary Index. A DynamoDB feature that allows you to query data using an alternate key.

JDBC
Java Database Connectivity. A Java API for connecting and executing queries with databases.

JMS
Java Message Service. A Java API for sending messages between two or more clients.

TPS
Transactions Per Second. A measure of the number of transactions a system can process in one second.

## AWS and System Terms
<a name="aws-and-system-terms"></a>

ARN
Amazon Resource Name. A unique identifier for AWS resources used to specify resources across AWS services.

ISO
International Organization for Standardization. An independent, non-governmental organization that develops international standards. Referenced in this guide for ISO 8601 timestamp format.

SLA
Service Level Agreement. A commitment between a service provider and a customer that defines the level of service expected.

UUID
Universally Unique Identifier. A 128-bit number used to uniquely identify information in computer systems.

vCPU
Virtual Central Processing Unit. A virtual processor assigned to a virtual machine or container, representing a portion of the physical CPU’s processing power.

## Load Testing Terms
<a name="load-testing-terms"></a>

concurrency
The number of concurrent virtual users per task. This parameter controls how many simulated users each Fargate task generates during a load test. Concurrency applies to Standard mode. In Native mode, the script sets its own virtual-user count.

Native mode
The traffic shape mode in which your uploaded script controls the load. In this mode, the solution runs the script under the testing framework’s own command line and passes no load parameters. It sets only the task count per Region and a safety duration.

regional stack
A CloudFormation stack deployed in an AWS Region to provide testing infrastructure for Multi-Region load tests.

safety duration
In Native mode, the maximum time a test is allowed to run, up to 24 hours. If the test is still running when the duration elapses, the solution stops the testing framework. It keeps the results for the portion that ran and records the run as complete.

Standard mode
The default traffic shape mode, in which the solution controls the load. You set the task count, concurrency, ramp-up period, and hold duration. The solution applies them through the Taurus automation framework, overriding the load your script declares.

task count
The number of Fargate containers (tasks) launched to run a test scenario. In Standard mode, the total load generated equals task count multiplied by concurrency. In Native mode, each task runs a full copy of your script. The total load equals task count multiplied by the load the script declares.

test scenario
A configured load test including test type, traffic shape mode, target endpoints, task count, concurrency, duration, and other parameters.

traffic shape mode
Which side controls the load a test generates, either Standard mode or Native mode.
