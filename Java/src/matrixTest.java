import org.opencv.core.*;

public class matrixTest {

	public static void main(String[] args) {
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		
		Mat matrix = new Mat(5, 5, CvType.CV_8UC1, new Scalar(0));  
		Mat row0 = matrix.row(0);
		
				
		row0.setTo(new Scalar(1));
		
		System.out.println(matrix.dump());
		
	}

}
