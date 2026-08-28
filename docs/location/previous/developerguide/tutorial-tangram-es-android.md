---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-es-android.html
---

# Using Tangram ES for Android with Amazon Location Service
<a name="tutorial-tangram-es-android"></a>

[Tangram ES](https://github.com/tangrams/tangram-es) is a C\+\+ library for rendering 2D and 3D maps from vector data using OpenGL ES. It's the native counterpart to [Tangram](https://github.com/tangrams/tangram).

Tangram styles built to work with the [Tilezen schema](https://tilezen.readthedocs.io/en/latest/layers/) are largely compatible with Amazon Location when using maps from HERE. These include:
+ [Bubble Wrap](https://github.com/tangrams/bubble-wrap) – A full-featured wayfinding style with helpful icons for points of interest.
+ [Cinnabar](https://github.com/tangrams/cinnabar-style) – A classic look and go-to for general mapping applications.
+ [Refill ](https://github.com/tangrams/refill-style)– A minimalist map style designed for data visualization overlays, inspired by the seminal Toner style by Stamen Design.
+ [Tron](https://github.com/tangrams/tron-style) – An exploration of scale transformations in the visual language of TRON.
+ [Walkabout ](https://github.com/tangrams/walkabout-style)– An outdoor-focused style that's perfect for hiking or getting out and about.

This guide describes how to integrate Tangram ES for Android with Amazon Location using the Tangram style called Cinnabar. This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

While other Tangram styles are best accompanied by raster tiles, which encode terrain information, this feature isn't yet supported by Amazon Location.

**Important**
The Tangram styles in the following tutorial are only compatible with Amazon Location map resources configured with the `VectorHereContrast` style.

## Building the application: Initialization
<a name="tutorial-tangram-es-android-initialization"></a>

To initialize your application:

1. Create a new Android Studio project from the **Empty Activity** template.

1. Ensure that **Kotlin** is selected for the project language.

1. Select a **Minimum SDK of API 16: Android 4.1 (Jelly Bean)** or newer.

1. Open **Project Structure** to select **File**, **Project Structure...**, and choose the **Dependencies** section.

1. With **<All Modules>** selected, choose the **\+** button to add a new **Library Dependency**.

1. Add **AWS Android SDK** version 2.19.1 or later. For example: `com.amazonaws:aws-android-sdk-core:2.19.1`

1. Add **Tangram** version 0.13.0 or later. For example: `com.mapzen.tangram:tangram:0.13.0`.
**Note**
Searching for **Tangram**: `com.mapzen.tangram:tangram:0.13.0` will generate a message that it's "not found", but choosing **OK** will allow it to be added.

## Building the application: Configuration
<a name="tutorial-tangram-es-android-configuration"></a>

To configure your application with your resources and AWS Region:

1. Create `app/src/main/res/values/configuration.xml`.

1. Enter the names and identifiers of your resources, and also the AWS Region they were created in:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="identityPoolId">{{us-east-1:54f2ba88-9390-498d-aaa5-0d97fb7ca3bd}}</string>
    <string name="mapName">{{TangramExampleMap}}</string>
    <string name="awsRegion">{{us-east-1}}</string>
    <string name="sceneUrl">https://www.nextzen.org/carto/cinnabar-style/9/cinnabar-style.zip</string>
    <string name="attribution">© 2020 HERE</string>
</resources>
```

## Building the application: Activity layout
<a name="tutorial-tangram-es-android-activity-layout"></a>

Edit `app/src/main/res/layout/activity_main.xml`:
+ Add a `MapView`, which renders the map. This will also set the map's initial center point.
+ Add a `TextView`, which displays attribution.

This will also set the map's initial center point.

**Note**
You must provide word mark or text attribution for each data provider that you use, either on your application or your documentation. Attribution strings are included in the style descriptor response under the `sources.esri.attribution`, `sources.here.attribution`, and `source.grabmaptiles.attribution` keys.
Because Tangram doesn't request these resources, and is only compatible with maps from HERE, use "© 2020 HERE". When using Amazon Location resources with [data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html), make sure to read the [service terms and conditions](https://aws.amazon.com/service-terms/).

```
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <com.mapzen.tangram.MapView
        android:id="@+id/map"
        android:layout_height="match_parent"
        android:layout_width="match_parent" />

    <TextView
        android:id="@+id/attributionView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:background="#80808080"
        android:padding="5sp"
        android:textColor="@android:color/black"
        android:textSize="10sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        tools:ignore="SmallSp" />
</androidx.constraintlayout.widget.ConstraintLayout>
```

## Building the application: Request transformation
<a name="tutorial-tangram-es-android-request-transformation"></a>

Create a class named `SigV4Interceptor` to intercept AWS requests and sign them using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This will be registered with the HTTP client used to fetch map resources when the Main Activity is created.

```
package aws.location.demo.okhttp

import com.amazonaws.DefaultRequest
import com.amazonaws.auth.AWS4Signer
import com.amazonaws.auth.AWSCredentialsProvider
import com.amazonaws.http.HttpMethodName
import com.amazonaws.util.IOUtils
import okhttp3.HttpUrl
import okhttp3.Interceptor
import okhttp3.Request
import okhttp3.Response
import okio.Buffer
import java.io.ByteArrayInputStream
import java.net.URI

class SigV4Interceptor(
    private val credentialsProvider: AWSCredentialsProvider,
    private val serviceName: String
) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val originalRequest = chain.request()

        if (originalRequest.url().host().contains("amazonaws.com")) {
            val signer = if (originalRequest.url().encodedPath().contains("@")) {
                // the presence of "@" indicates that it doesn't need to be double URL-encoded
                AWS4Signer(false)
            } else {
                AWS4Signer()
            }

            val awsRequest = toAWSRequest(originalRequest, serviceName)
            signer.setServiceName(serviceName)
            signer.sign(awsRequest, credentialsProvider.credentials)

            return chain.proceed(toSignedOkHttpRequest(awsRequest, originalRequest))
        }

        return chain.proceed(originalRequest)
    }

    companion object {
        fun toAWSRequest(request: Request, serviceName: String): DefaultRequest<Any> {
            // clone the request (AWS-style) so that it can be populated with credentials
            val dr = DefaultRequest<Any>(serviceName)

            // copy request info
            dr.httpMethod = HttpMethodName.valueOf(request.method())
            with(request.url()) {
                dr.resourcePath = uri().path
                dr.endpoint = URI.create("${scheme()}://${host()}")

                // copy parameters
                for (p in queryParameterNames()) {
                    if (p != "") {
                        dr.addParameter(p, queryParameter(p))
                    }
                }
            }

            // copy headers
            for (h in request.headers().names()) {
                dr.addHeader(h, request.header(h))
            }

            // copy the request body
            val bodyBytes = request.body()?.let { body ->
                val buffer = Buffer()
                body.writeTo(buffer)
                IOUtils.toByteArray(buffer.inputStream())
            }

            dr.content = ByteArrayInputStream(bodyBytes ?: ByteArray(0))

            return dr
        }

        fun toSignedOkHttpRequest(
            awsRequest: DefaultRequest<Any>,
            originalRequest: Request
        ): Request {
            // copy signed request back into an OkHttp Request
            val builder = Request.Builder()

            // copy headers from the signed request
            for ((k, v) in awsRequest.headers) {
                builder.addHeader(k, v)
            }

            // start building an HttpUrl
            val urlBuilder = HttpUrl.Builder()
                .host(awsRequest.endpoint.host)
                .scheme(awsRequest.endpoint.scheme)
                .encodedPath(awsRequest.resourcePath)

            // copy parameters from the signed request
            for ((k, v) in awsRequest.parameters) {
                urlBuilder.addQueryParameter(k, v)
            }

            return builder.url(urlBuilder.build())
                .method(originalRequest.method(), originalRequest.body())
                .build()
        }
    }
}
```

## Building the application: Main activity
<a name="tutorial-tangram-es-android-request-main-activity"></a>

The Main Activity is responsible for initializing the views that will be displayed to users. This involves:
+ Instantiating an Amazon Cognito `CredentialsProvider`.
+ Registering the Signature Version 4 interceptor.
+ Configuring the map by pointing it at a map style, overriding tile URLs, and displaying appropriate attribution.

`MainActivity` is also responsible for forwarding life cycle events to the map view.

```
package aws.location.demo.tangram

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import aws.location.demo.okhttp.SigV4Interceptor
import com.amazonaws.auth.CognitoCachingCredentialsProvider
import com.amazonaws.regions.Regions
import com.mapzen.tangram.*
import com.mapzen.tangram.networking.DefaultHttpHandler
import com.mapzen.tangram.networking.HttpHandler

private const val SERVICE_NAME = "geo"

class MainActivity : AppCompatActivity(), MapView.MapReadyCallback {
    private var mapView: MapView? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_main)

        mapView = findViewById(R.id.map)

        mapView?.getMapAsync(this, getHttpHandler())
        findViewById<TextView>(R.id.attributionView).text = getString(R.string.attribution)
    }

    override fun onMapReady(mapController: MapController?) {
        val sceneUpdates = arrayListOf(
            SceneUpdate(
                "sources.mapzen.url",
                "https://maps.geo.${getString(R.string.awsRegion)}.amazonaws.com/maps/v0/maps/${
                    getString(
                        R.string.mapName
                    )
                }/tiles/{z}/{x}/{y}"
            )
        )

        mapController?.let { map ->
            map.updateCameraPosition(
                CameraUpdateFactory.newLngLatZoom(
                    LngLat(-123.1187, 49.2819),
                    12F
                )
            )
            map.loadSceneFileAsync(
                getString(R.string.sceneUrl),
                sceneUpdates
            )
        }
    }

    private fun getHttpHandler(): HttpHandler {
        val builder = DefaultHttpHandler.getClientBuilder()

        val credentialsProvider = CognitoCachingCredentialsProvider(
            applicationContext,
            getString(R.string.identityPoolId),
            Regions.US_EAST_1
        )

        return DefaultHttpHandler(
            builder.addInterceptor(
                SigV4Interceptor(
                    credentialsProvider,
                    SERVICE_NAME
                )
            )
        )
    }

    override fun onResume() {
        super.onResume()
        mapView?.onResume()
    }

    override fun onPause() {
        super.onPause()
        mapView?.onPause()
    }

    override fun onLowMemory() {
        super.onLowMemory()
        mapView?.onLowMemory()
    }

    override fun onDestroy() {
        super.onDestroy()
        mapView?.onDestroy()
    }
}
```

Running this application displays a full-screen map in the style of your choosing. This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
