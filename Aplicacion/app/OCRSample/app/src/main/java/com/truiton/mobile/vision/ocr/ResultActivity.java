package com.truiton.mobile.vision.ocr;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.Iterator;

public class ResultActivity extends AppCompatActivity {
    private TextView result_tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);
        result_tv = (TextView) findViewById(R.id.results_tv);
        Intent intent = getIntent();
        try {
            JSONObject payload = new JSONObject(intent.getStringExtra("payload"));
            showJson(payload);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    private void showJson(JSONObject payload) throws JSONException {
        Iterator <String> keys = payload.keys();
        String key;
        while (keys.hasNext()){
            key = keys.next();
            showAdditive(payload.getJSONObject(key));
        }

    }
    private void showAdditive(JSONObject additive){
        String id,tipo,aditivo,aditivos_alergicos;
        try {
            id = additive.getString("id");
            aditivo = additive.getString("aditivo");
            tipo = additive.getString("tipo");
            aditivos_alergicos = additive.getString("aditivos_alergicos");
            result_tv.setText(result_tv.getText().toString()+id+": " +aditivo+"\n"+tipo+"\n"+aditivos_alergicos+"\n\n");
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}
