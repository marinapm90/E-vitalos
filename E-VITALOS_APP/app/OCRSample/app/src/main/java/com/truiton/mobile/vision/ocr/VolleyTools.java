package com.truiton.mobile.vision.ocr;

import android.content.Context;

import com.android.volley.RequestQueue;
import com.android.volley.toolbox.Volley;

public class VolleyTools {
    private static RequestQueue queue;

    public static RequestQueue getQueue(Context context){
        if (queue == null){
            queue = Volley.newRequestQueue(context);

        }
        return queue;
    }
}
