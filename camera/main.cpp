#include <opencv2/opencv.hpp>
#include <sstream>  // For creating filenames

int main() {
    cv::VideoCapture cap(0);

    if (!cap.isOpened()) {
        std::cerr << "Error: Could not open camera." << std::endl;
        return -1;
    }

    cv::namedWindow("Camera Feed", cv::WINDOW_NORMAL);
    cap.set(cv::CAP_PROP_FRAME_WIDTH, 640);
    cap.set(cv::CAP_PROP_FRAME_HEIGHT, 480);

    double desiredFPS = 3.0;  // Capture one image per second
    int delayBetweenFrames = static_cast<int>(1000.0 / desiredFPS);

    cv::Mat frame;
    int frameCount = 0;

    while (true) {
        cap >> frame;

        if (frame.empty()) {
            std::cerr << "Error: No frame captured." << std::endl;
            break;
        }

        // Display the captured frame
        cv::imshow("Camera Feed", frame);

        // Save the frame as an image file
        std::ostringstream filename;
        filename << "frame_" << frameCount << ".jpg";
        cv::imwrite(filename.str(), frame);

        frameCount++;

        if (cv::waitKey(delayBetweenFrames) == 27) {
            break;
        }
    }

    cap.release();
    cv::destroyAllWindows();

    return 0;
}
