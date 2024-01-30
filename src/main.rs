use eframe::egui;

// Function to calculate Fibonacci number
fn fib(n: i32) -> i32 {
    if n <= 1 {
        n
    } else {
        fib(n - 1) + fib(n - 2)
    }
}

fn main() {
    // Set up native options
    let native_options = eframe::NativeOptions::default();
    
    // Run the native eframe app
    eframe::run_native("My egui App", native_options, Box::new(|cc| Box::new(MyEguiApp::new(cc))));
}

#[derive(Default)]
struct MyEguiApp {}

impl MyEguiApp {
    // Create a new instance of MyEguiApp
    fn new(_cc: &eframe::CreationContext<'_>) -> Self {
        // Customize egui here with cc.egui_ctx.set_fonts and cc.egui_ctx.set_visuals.
        // Restore app state using cc.storage (requires the "persistence" feature).
        // Use the cc.gl (a glow::Context) to create graphics shaders and buffers that you can use
        // for e.g. egui::PaintCallback.
        Self::default()
    }
}

impl eframe::App for MyEguiApp {
    // Update method for the eframe app
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        // Show the central panel
        egui::CentralPanel::default().show(ctx, |ui| {
            // Display Fibonacci numbers in a loop
            for i in 0..=20 {
                ui.label(format!("fib({}) = {}", i, fib(i)));
            }
        });
    }
}
