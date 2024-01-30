use ggez::{event, graphics, Context, GameResult, conf};
use lazy_static::lazy_static;


// declaration and initialization of constant global variables
lazy_static! {
    static ref SCREEN_WIDTH: f32 = 1280.0;
    static ref SCREEN_HEIGHT: f32 = 720.0;
}


struct MainState {
    pos_x: f32,
}

impl MainState {
    fn new() -> GameResult<MainState> {
        let s = MainState { pos_x: 0.0 };
        Ok(s)
    }
}

impl event::EventHandler<ggez::GameError> for MainState {
    fn update(&mut self, _ctx: &mut Context) -> GameResult {
        self.pos_x = (self.pos_x + 1.0) % 800.0;
        Ok(())
    }

    fn draw(&mut self, ctx: &mut Context) -> GameResult {
        let mut canvas =
            graphics::Canvas::from_frame(ctx, graphics::Color::from([1.0, 1.0, 1.0, 0.0]));

        // draw a rectangle in the middle of the screen
        let rect_length = 100.0;
        let rect_height = 100.0;

        let rect = graphics::Mesh::new_rectangle(
            ctx,
            graphics::DrawMode::fill(),
            graphics::Rect::new(
                *SCREEN_WIDTH / 2.0 - (rect_length / 2.0),
                *SCREEN_HEIGHT / 2.0 - (rect_length / 2.0),
                rect_height,
                rect_length,
            ),
            graphics::Color::from([0.0, 0.0, 0.0, 1.0]),
        )?;
        canvas.draw(&rect, graphics::DrawParam::default());

        canvas.finish(ctx)?;
        Ok(())
    }
}

pub fn main() -> GameResult {
    
    // Create a context builder with window dimensions
    let cb = ggez::ContextBuilder::new("super_simple", "mbn")
        .window_setup(conf::WindowSetup::default().title("Your Game Title"))
        .window_mode(conf::WindowMode::default().dimensions(*SCREEN_WIDTH, *SCREEN_HEIGHT));

    let (ctx, event_loop) = cb.build()?;
    let state = MainState::new()?;
    event::run(ctx, event_loop, state)

}
