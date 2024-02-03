use ggez::{conf, event, graphics, Context, GameResult};
use lazy_static::lazy_static;

// For keyboard input use
// use ggez::input::keyboard::KeyCode;

// declaration and initialization of constant global variables
lazy_static! {
    static ref SCREEN_WIDTH: f32 = 1280.0;
    static ref SCREEN_HEIGHT: f32 = 720.0;
}

struct MainState {
    _pos_x: f32,
    _pos_y: f32,
}

impl MainState {
    fn new() -> GameResult<MainState> {
        let s = MainState { _pos_x: 0.0 , _pos_y: 0.0};
        Ok(s)
    }
}

fn fibonacci(n: u32) -> u32 {
    
    let mut _arr: Vec<u32> = Vec::new();


    if n == 0 {
        return 0;
    }
    if n == 1 {
        return 1;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

impl event::EventHandler<ggez::GameError> for MainState {
    fn update(&mut self, _ctx: &mut Context) -> GameResult {

        Ok(())
    }

    fn draw(&mut self, ctx: &mut Context) -> GameResult {
        let canvas =
            graphics::Canvas::from_frame(ctx, graphics::Color::from([1.0, 1.0, 1.0, 0.0]));




            
        canvas.finish(ctx)?;
        Ok(())
    }
}

pub fn main() -> GameResult {
    
    fibonacci(10);

    // Create a context builder with window dimensions
    let cb = ggez::ContextBuilder::new("super_simple", "mbn")
        .window_setup(conf::WindowSetup::default().title("Your Game Title"))
        .window_mode(conf::WindowMode::default().dimensions(*SCREEN_WIDTH, *SCREEN_HEIGHT));

    let (ctx, event_loop) = cb.build()?;
    let state = MainState::new()?;
    event::run(ctx, event_loop, state)

}
