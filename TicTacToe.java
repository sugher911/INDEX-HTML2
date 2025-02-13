import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class TicTacToe implements ActionListener {
    private JFrame frame;
    private JButton[] buttons;
    private boolean playerXTurn = true;
    private Random random;
    
    public TicTacToe() {
        frame = new JFrame("Tic Tac Toe");
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(3, 3));
        frame.getContentPane().setBackground(Color.red); // Set background color
        
        buttons = new JButton[9];
        random = new Random();
        
        for (int i = 0; i < 9; i++) {
            buttons[i] = new JButton("");
            buttons[i].setFont(new Font("Arial", Font.PLAIN, 40));
            buttons[i].setForeground(Color.white); // Set default font color
            buttons[i].setFocusPainted(false);
            buttons[i].addActionListener(this);
            frame.add(buttons[i]);
        }
        
        frame.setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        JButton clickedButton = (JButton) e.getSource();
        if (!clickedButton.getText().equals("")) {
            return;
        }
        
        clickedButton.setText(playerXTurn ? "X" : "O");
        clickedButton.setForeground(playerXTurn ? Color.blue : Color.green); // Change font color based on player
        clickedButton.setBackground(getRandomColor()); // Change button color each time it's clicked
        playerXTurn = !playerXTurn;
        
        checkWinner();
    }
    
    private Color getRandomColor() {
        return new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256));
    }
    
    private void checkWinner() {
        int[][] winningCombinations = {
            {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
            {0, 4, 8}, {2, 4, 6}
        };
        
        for (int[] combo : winningCombinations) {
            String b1 = buttons[combo[0]].getText();
            String b2 = buttons[combo[1]].getText();
            String b3 = buttons[combo[2]].getText();
            
            if (!b1.equals("") && b1.equals(b2) && b2.equals(b3)) {
                JOptionPane.showMessageDialog(frame, "Player " + b1 + " wins!");
                resetGame();
                return;
            }
        }
        
        boolean draw = true;
        for (JButton button : buttons) {
            if (button.getText().equals("")) {
                draw = false;
                break;
            }
        }
        
        if (draw) {
            JOptionPane.showMessageDialog(frame, "It's a draw!");
            resetGame();
        }
    }
    
    private void resetGame() {
        for (JButton button : buttons) {
            button.setText("");
            button.setForeground(Color.white); // Reset font color
            button.setBackground(null); // Reset button color
        }
        playerXTurn = true;
    }
    
    public static void main(String[] args) {
        new TicTacToe();
    }
}
