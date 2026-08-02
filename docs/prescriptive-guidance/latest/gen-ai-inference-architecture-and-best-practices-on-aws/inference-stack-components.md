---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/inference-stack-components.html
---

# Components of an AI inference stack
<a name="inference-stack-components"></a>

A production AI inference stack typically consists of the following three core components:
+ End user application – Serves as the entry point for user interactions and request handling
+ Inference API server (inference frontend) – Manages API serving and request processing
+ Inference backend – Handles the core model execution and resource management

These components communicate through standardized protocols like [gRPC](https://grpc.io/about/) for reliable and efficient model serving. The following diagram shows the high-level architecture of a real-time inference workload. It showcases the core components and how they communicate with each other.

![Architecture showing core components of production AI inference stack.](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/735c174b-b85d-4ef7-ad78-3e83ba821267.png)

This section provides details about each component.

## End user application
<a name="end-user-application"></a>

The end user application component serves as the initial touchpoint for all client interactions, providing a secure and controlled entry point to the inference system. It incorporates essential security features like authentication through tokens and keys, implements throttling mechanisms to prevent system overload, and includes queuing capabilities to manage high request volumes. Some emerging tools use proxies and load balancers to enable key provisioning, multi-tenant or multi-user throttling, queueing, and automatic failover in multi-region scenarios. Examples of these emerging tools include [LiteLLM](https://www.litellm.ai/), [Portkey](https://portkey.ai/), and [Kong AI Gateway](https://konghq.com/products/kong-ai-gateway).

## Inference API server or frontend
<a name="inference-api-server"></a>

Acting as the bridge between client requests and model execution, the frontend component provides a robust API server that orchestrates the flow of inference requests. This component implements sophisticated request handling mechanisms including the following:
+ Request batching for improved throughput
+ Intelligent routing to distribute load across available workers
+ Queue management for optimal request processing
+ Comprehensive metrics collection to monitor system performance

The frontend communicates with the backend through standardized gRPC protocols, ensuring reliable and efficient data transfer. Popular frontends include [NVIDIA Triton](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/backend/README.html), [NVIDIA Dynamo](https://docs.nvidia.com/dynamo/latest/), [Deep Java Library (DJL)](https://docs.djl.ai/master/docs/serving/serving/docs/lmi/deployment_guide/backend-selection.html), [Ray Serve](https://docs.ray.io/en/latest/serve/getting_started.html), and [Text Generation Inference (TGI)](https://huggingface.co/blog/tgi-multi-backend) from Hugging Face.

## Inference backend
<a name="inference-backend"></a>

The inference backend is where the model execution takes place, managed by specialized workers that handle the computational heavy lifting. The backend component is responsible for critical functions such as the following:
+ Memory management to optimize resource utilization
+ Model loading and initialization to ensure efficient startup
+ Computation-level batching for improved throughput
+ Performance metrics tracking

It works in close coordination with the frontend component to process requests while managing system resources effectively to maintain optimal performance and reliability. You can use a Python backend where you write your own inference logic. You can also use more optimized and popular backends such as [vLLM](https://docs.vllm.ai/en/latest/), [TensorRT LLM](https://nvidia.github.io/TensorRT-LLM/), [ONNX Runtime](https://onnxruntime.ai/), and [SGLang](https://docs.sglang.io/). The backend component also maintains a connection to model storage, which houses various model formats including [Safetensors](https://huggingface.co/docs/safetensors/en/index), [GGUF, ONNX](https://onnx.ai/onnx/intro/), [NeMo](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/checkpoints/intro.html), [NEFF](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/neuron-runtime/explore/work-with-neff-files.html), and Hugging Face models. This capability helps provide efficient access to the required model checkpoints.
