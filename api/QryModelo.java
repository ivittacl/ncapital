import java.io.*;
import hex.genmodel.easy.RowData;
import hex.genmodel.easy.EasyPredictModelWrapper;
import hex.genmodel.easy.prediction.*;
import hex.genmodel.MojoModel;
import py4j.GatewayServer;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.Date;

public class QryModelo {
  public String qry_modelo( 
    String DifPre, 
    String EstDoc, 
    String Mora, 
    String DiscriminarorMora, 
    String RMora,
    String IvaCom,
    String MonAnt,
    String MonDoc,
    String SalCli,
    String TipDoc,
    String MGO,
    String CTO,
    String PCO,
    String MAO,
    String TGO,
    String dias,
    String ClasifCliente,
    String RutCliDeu,
    String ClasDeu,
    String DisCriminadorCastigo
)
    throws Exception {
    EasyPredictModelWrapper model = new EasyPredictModelWrapper(MojoModel.load("DRF_model_R_1544446312064_6.zip"));

    RowData row = new RowData();
    row.put("DifPre", DifPre);
    row.put("EstDoc", EstDoc);
    row.put("Mora", Mora);
    row.put("DiscriminarorMora", DiscriminarorMora);
    row.put("RMora", RMora);
    row.put("IvaCom", IvaCom);
    row.put("MonAnt", MonAnt);
    row.put("MonDoc", MonDoc);
    row.put("SalCli", SalCli);
    row.put("TipDoc", TipDoc);
    row.put("MGO", MGO);
    row.put("CTO", CTO);
    row.put("PCO", PCO);
    row.put("MAO", MAO);
    row.put("TGO", TGO);
    row.put("dias", dias);
    row.put("ClasifCliente", ClasifCliente);
    row.put("RutCliDeu", RutCliDeu);
    row.put("ClasDeu", ClasDeu);
    row.put("DisCriminadorCastigo", DisCriminadorCastigo);
    System.out.println("===============================================");
    DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
    Date date = new Date();
    System.out.println(dateFormat.format(date));
    System.out.print("DifPre: ");
    System.out.println(DifPre);
    System.out.print("EstDoc: ");
    System.out.println(EstDoc);
    System.out.print("Mora: ");
    System.out.println(Mora);
    System.out.print("DiscriminarorMora: ");
    System.out.println(DiscriminarorMora);
    System.out.print("RMora: ");
    System.out.println(RMora);
    System.out.print("IvaCom: ");
    System.out.println(IvaCom);
    System.out.print("ClasifCliente: ");
    System.out.println(ClasifCliente);
    System.out.print("ClasDeu: ");
    System.out.println(ClasDeu);

    RegressionModelPrediction p = model.predictRegression(row);
    String lstrResult="";
    lstrResult = String.valueOf(p.value);
    System.out.print("lstrResult: ");
    System.out.println(lstrResult);
    return lstrResult;
  }
  
  public static void main(String[] args) {
    QryModelo app = new QryModelo();
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(app);
    server.start();
  }
}
