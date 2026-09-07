---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/virtual-channel-api.html
---

# Virtual Channel API
<a name="virtual-channel-api"></a>

## SetupVirtualChannel
<a name="setupvirtualchannel"></a>

When a client extension and a server extension want to exchange data, they can setup a virtual channel between each other.

Both parties will issue a `SetupVirtualChannelRequest` message and both will wait for a `VirtualChannelReadyEvent` message. The synchronous response contains the name of the relay (named pipe on Windows, abstract UNIX domain socket on Linux and UNIX domain socket on macOS) over which the extensions will exchange data with Amazon DCV and an authentication token used by Amazon DCV to validate the process that is connecting to the relay endpoint.
+ The caller must establish the communication with DCV.

  For Windows, open the client side of the named pipe.

  For Linux, open the abstract UNIX domain socket.

  For macOS, open the UNIX domain socket.
+ Send the authentication token to the data channel.
+ Wait for the asynchronous event on the control channel before writing any other data to it.

The caller must specify the ID of the process that will open the client side of the relay, Amazon DCV will reject any attempt to connect to the relay from another process. Should the extension use the virtual channel from another process (e.g. a daemon process crashes and it is re-spawned), it will need to undergo a new virtual channel setup procedure.

The maximum number of open virtual channels (established or pending) for one extension is four, further setup requests will fail.

![Sequence diagram showing virtual channel setup between Extension Client, DCV Client, and DCV Server.](https://docs.aws.amazon.com/dcv/latest/extsdkguide/images/setup-virtual-channel.jpg)

**Request message:**

```
SetupVirtualChannelRequest
+ string virtual_channel_name
+ int64 relay_client_process_id
```
+ **virtual\_channel\_name**: Specific name of the virtual channel, the namespace is taken from the manifest.
+ **relay\_client\_process\_id**: Pid of the process that will open the client side of the relay.

**Response message:**

```
SetupVirtualChannelResponse
+ string virtual_channel_name
+ string relay_path
+ int64 relay_client_process_id
+ bytes virtual_channel_auth_token
```
+ **virtual\_channel\_name**: Specific name of the virtual channel to be set up. The namespace is taken from the manifest.
+ **relay\_path**: Full path of the relay to the virtual channel. On Windows, it is the name of a named pipe. On Linux, it is the name of the abstract UNIX domain socket. On macOS, it is the name of the UNIX domain socket.
**Example**

  For example:`\\.\pipe\dcvextensions_random`
+ **relay\_client\_process\_id**: The pid of the process that runs the server side of the relay client: the Amazon DCV viewer on clients, the Amazon DCV server process on servers.
+ **virtual\_channel\_auth\_token**: An authentication token the process has to send on the relay channel. DCV will use it to validate the connecting process.

**Event message:**

```
VirtualChannelReadyEvent
+ string virtual_channel_name
```
+ **virtual\_channel\_name**: Specific name of the virtual channel, the namespace is taken from the manifest.

## CloseVirtualChannel
<a name="closevirtualchannel"></a>

One party (either the client extension or the server extension) can initiate the closure of a virtual channel with a `CloseVirtualChannelRequest`, the other party will be notified with a `VirtualChannelClosedEvent`.

![Sequence diagram showing CloseVirtualChannelRequest and Response between DCV components, followed by VirtualChannelClosedEvent.](https://docs.aws.amazon.com/dcv/latest/extsdkguide/images/close-virtual-channel.jpg)

**Request message:**

```
CloseVirtualChannelRequest
+ string virtual_channel_name
```
+ **Request message:****virtual\_channel\_name**: Specific name of the virtual channel, the namespace is taken from the manifest.

**Response message:**

```
CloseVirtualChannelResponse
+ string virtual_channel_name
```
+ **virtual\_channel\_name**: Specific name of the virtual channel to be set up, the namespace is taken from the manifest.

**Event message:**

```
VirtualChannelClosedEvent
+ string virtual_channel_name
```
+ **virtual\_channel\_name**: Specific name of the virtual channel, the namespace is taken from the manifest.
