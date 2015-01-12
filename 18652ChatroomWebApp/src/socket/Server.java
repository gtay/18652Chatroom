package socket;

import java.io.IOException;
import java.io.StringWriter;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

import org.json.*;

import javax.websocket.server.ServerEndpoint;
import javax.websocket.OnClose;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;

@ServerEndpoint("/chatroomServer")
public class Server {
	static Set<Session> users = Collections.synchronizedSet(new HashSet<Session>());

	@OnOpen
	public void handleOpen(Session userSession) {
		users.add(userSession);
	}
	
	@OnMessage
	public void handleMessage(String message, Session userSession) throws IOException, JSONException {
		String username = (String) userSession.getUserProperties().get("username");
		
		//handle username cases
		if (username == null) {
			userSession.getUserProperties().put("username", message);
			userSession.getBasicRemote().sendText(JSONBuilder("Admin","you are now connected as: " + message));
		} else {
			Iterator<Session> iterator = users.iterator();
			while (iterator.hasNext()) {
				iterator.next().getBasicRemote().sendText(JSONBuilder(username, message));
			}
		}
	}
	
	private String JSONBuilder(String username, String message) throws JSONException {
		//StringWriter sWriter = new StringWriter();
		JSONObject jsonObject = new JSONObject().put("message", username + ": " + message);
		//JSONWriter jsonWriter = new JSONWriter(sWriter);
		//jsonWriter.
		return jsonObject.toString();
	}

	@OnClose
	public void handleClose(Session userSession) {
		users.remove(userSession);
	}
}
