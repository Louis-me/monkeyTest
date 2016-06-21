package com.example.monkneytest;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
public class MainActivity extends Activity {
	Button btn;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
	
		setContentView(R.layout.activity_main);
		btn = (Button) findViewById(R.id.btn1);
		btn.setOnClickListener(newOnClickListener);  
		
	}
	private OnClickListener newOnClickListener = new OnClickListener(){
		@Override
		public void onClick(View v) {
			String a =null; a.toString();
		}
	};

}
