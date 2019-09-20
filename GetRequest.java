import java.io.*;
import java.net.*;

public class GetRequest {


    public static void main(String[] args) throws Exception {

        GetRequest getReq = new GetRequest();

        //Runs SendReq passing in the url and port from the command line
        getReq.SendReq("www.amazon.com", 80);
		//getReq.SendPut("www.amazon.com", 80);
    }

    public void SendReq(String url, int port) throws Exception {

        //Instantiate a new socket
        Socket s = new Socket("www.amazon.com", port);

        //Instantiates a new PrintWriter passing in the sockets output stream
        PrintWriter wtr = new PrintWriter(s.getOutputStream());

        //Prints the request string to the output stream
        wtr.println("GET / HTTP/1.1");
        wtr.println("Host: amazon.com");
        wtr.println("");
        wtr.flush();

        //Creates a BufferedReader that contains the server response
        BufferedReader bufRead = new BufferedReader(new InputStreamReader(s.getInputStream()));
        String outStr;

        //Prints each line of the response 
        while((outStr = bufRead.readLine()) != null){
            System.out.println(outStr);
        }


        //Closes out buffer and writer
        bufRead.close();
        wtr.close();

    }
	/**public void SendPut(String url, int port) throws Exception {
		HttpURLConnection httpCon = (HttpURLConnection) url.openConnection();
		httpCon.setDoOutput(true);
		httpCon.setRequestMethod("PUT");
		OutputStreamWriter out = new OutputStreamWriter(
    		httpCon.getOutputStream());
		out.write("Resource content");
		out.close();
		httpCon.getInputStream();
		**/

	}
}