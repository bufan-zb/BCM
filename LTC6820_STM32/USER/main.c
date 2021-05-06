#include "stm32f10x.h"
#include "sys.h"
#include "delay.h"
#include "usart.h"
#include "LTC6804-1.h"
#include "spi.h"

#define LED  GPIO_Pin_13
#define LED_ON  {GPIO_SetBits(GPIOD,LED);} 
#define LED_OFF {GPIO_ResetBits(GPIOD,LED);} 
//void SysTick_Handler(void);
void GPIO_Configuration(void);
void RCC_Configuration(void);
void USART_Config(void);
void DMA_Configuration(void);
void NVIC_Config(void);  

void uart_sendInt(uint16_t sendData);
unsigned char read_cfgr[2][8];
uint16_t    cell_codes[15][12];
uint16_t    cellCodes[180];
unsigned int cell_voltage[15][12];
uint16_t gpio_codes[1][6];
unsigned char temperature[30];//�¶ȣ�ȡ�������磺26��,����û��
unsigned int stat_codes[2][6];
unsigned char cell_zu=15;//���干�м�����
unsigned char i;

unsigned char write_cfgr[15][6]={0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00,
                                0x1c,0x00,0x00,0x00,0x00,0x00}; //�ŵ�����

uint8_t  box,group;//

void Delay(u32 count)
{
u32 i=0;
for(;i<count;i++);
}


char error_flag1,error_flag2;
extern vu32 TimingDelay ;

int main(void)
{
  RCC_Configuration();
  GPIO_Configuration();
  //NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
  NVIC_Config() ;
  SysTick_Config(9000000);
  SysTick_CLKSourceConfig(SysTick_CLKSource_HCLK_Div8);//SysTick_CLKSource_HCLK_Div8  SysTick_CLKSource_HCLK
  LTC6804_initialize();  //��ʼ��LTC6804
  //uart_init(115200);
  USART_Config();
  DMA_Configuration();
  while(1)
    {
      if((TimingDelay%7)==0)
        {
          LED_ON
          LTC6804_adcvax();//������ϵ�ص�ѹ�Լ�GPIO1��GPIO2ת������ѯ״̬
                         //�˾������� LTC6804_rdcv���ǰ�����򲿷ֵ�ص�ѹ�����޷�����
                         //ÿ�ζ���ص�ѹ���뷢������
//          error_flag1=LTC6804_rdcv(0,cell_zu,cell_codes);
//          error_flag2=LTC6804_rdaux(1,cell_zu,gpio_codes);//��LTC6804���¶ȴ�������ѹֵ

         LTC6804_rdcv(0,cell_zu,cell_codes);
//         LTC6804_rdaux(1,cell_zu,gpio_codes);//��LTC6804���¶ȴ�������ѹֵ
//         LTC6804_adcvax();
//         DMA_Cmd(DMA1_Channel4, ENABLE);

//       uart_sendInt(cell_codes[0][0]);
//			
//       for(i=0;i<12;i++)
//         {
//		    uart_sendInt(cell_codes[0][i]);
//			}
//		for(box=0;box<15;box=box+2)
//		{ 
//			for(group=0;group<12;group++)
//			{	
//				printf("cells[%2d][%2d]=%d",box,group,cell_codes[box][group]);
//				
//				if(box!=14) 
//				{
//					printf("\t");printf("\t");
//					printf("cells[%2d][%2d]=%d\r\n",box+1,group,cell_codes[box+1][group]);
//				}
//				if(box==14) printf("\r\n");	
//			}
//					
//			printf("\r\n");
//		}
}
    else
      LED_OFF



}
}

/*******************************************************************************
* ������  		: GPIO_Configuration
* ��������    	: ���ø�GPIO�˿ڹ���
* �������      : ��
* ������      : ��
* ����ֵ        : ��
*******************************************************************************/

void GPIO_Configuration(void)
{ 
	
	/* ���� GPIO ��ʼ���ṹ�� GPIO_InitStructure */
	GPIO_InitTypeDef GPIO_InitStructure;
//	
	//RCC_APB2PeriphClockCmd(	RCC_APB2Periph_GPIOD|RCC_APB2Periph_GPIOA, ENABLE );//PORTBʱ��ʹ�� 
  	
	/* ���� SPI1 ����: SCK, MISO �� MOSI */
//	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
//	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
//	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
//	GPIO_Init(GPIOA, &GPIO_InitStructure);
	
    	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3 ;//����SPI cs�ź���PA3
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(GPIOA, &GPIO_InitStructure);

  RCC_APB2PeriphClockCmd(	RCC_APB2Periph_GPIOD, ENABLE );//PORTDʱ��ʹ��	,��������LED����˸����
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13 ;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(GPIOD, &GPIO_InitStructure);
	
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;	         		 //USART1 TX
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;    		 //�����������	������� Push-pull output
  
  GPIO_Init(GPIOA, &GPIO_InitStructure);		    		 //A�˿� 

  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;	         	 //USART1 RX
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;   	 //���ÿ�©����
  GPIO_Init(GPIOA, &GPIO_InitStructure);
	
}

void USART_Config(void)
{
  USART_InitTypeDef USART_InitStructure;
  USART_InitStructure.USART_BaudRate 	= 115200;						//����115200bps
  USART_InitStructure.USART_WordLength 	= USART_WordLength_8b;		//����λ8λ
  USART_InitStructure.USART_StopBits 	= USART_StopBits_1;			//ֹͣλ1λ
  USART_InitStructure.USART_Parity 		= USART_Parity_No;				//��У��λ
  USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;   //��Ӳ������
  USART_InitStructure.USART_Mode 		=  USART_Mode_Tx;					//�շ�ģʽ USART_Mode_Rx |

  USART_Init(USART1, &USART_InitStructure);							//���ô��ڲ�������
  USART_DMACmd(USART1, USART_DMAReq_Tx, ENABLE);
  USART_Cmd(USART1, ENABLE);	
}

 /*******************************************************************************
* ������		: RCC_Configuration
* ��������  	: ����ϵͳ������ʱ��
* �������  	: ��
* ������  	: ��
* ����ֵ    	: ��
*******************************************************************************/

void RCC_Configuration(void)
{
	//--------------------------- CLK INIT, HSE PLL ----------------------------
		ErrorStatus HSEStartUpStatus;
		//RCC reset
		RCC_DeInit();
		//�����ⲿʱ�� ��ִ�г�ʼ��
		RCC_HSEConfig(RCC_HSE_ON); 
		//�ȴ��ⲿʱ��׼����
		HSEStartUpStatus = RCC_WaitForHSEStartUp();
		//����ʧ�� ������ȴ�
		while(HSEStartUpStatus == ERROR);
		//�����ڲ�����ʱ��
		RCC_HCLKConfig(RCC_SYSCLK_Div1);
		RCC_PCLK1Config(RCC_HCLK_Div1);
		RCC_PCLK2Config(RCC_HCLK_Div1);
		//�ⲿʱ��Ϊ8M ���ﱶƵ��72M
		RCC_PLLConfig(RCC_PLLSource_HSE_Div1, RCC_PLLMul_9);
		RCC_PLLCmd(ENABLE); 
		while(RCC_GetFlagStatus(RCC_FLAG_PLLRDY) == RESET);
		RCC_SYSCLKConfig(RCC_SYSCLKSource_PLLCLK);
		while(RCC_GetSYSCLKSource() != 0x08);

		//----------------------------- CLOSE HSI ---------------------------
		//�ر��ڲ�ʱ��HSI
		RCC_HSICmd(DISABLE);	

		//--------------------------- OPEN GPIO CLK -------------------------
		RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);


   RCC_APB1PeriphClockCmd(RCC_APB1Periph_PWR | RCC_APB1Periph_BKP, ENABLE);
	/* �� SPI2 ʱ�� */
	//RCC_APB1PeriphClockCmd(RCC_APB1Periph_SPI2, ENABLE);
	/* �� GPIOA��GPIOB��USART1 �� SPI1 ʱ�� */
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA |RCC_APB2Periph_GPIOD|
						   RCC_APB2Periph_USART1 |RCC_APB2Periph_SPI1, ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE); //��DMAʱ�� 
	RCC_APB2PeriphClockCmd( RCC_APB2Periph_USART1, ENABLE); 
}

void DMA_Configuration(void)
{ 
  DMA_InitTypeDef DMA_InitStructure;
  DMA_DeInit(DMA1_Channel4);
  DMA_InitStructure.DMA_PeripheralBaseAddr 	= (uint32_t)(uint32_t)&USART1->DR; 
  DMA_InitStructure.DMA_MemoryBaseAddr 		= (uint32_t)cell_codes;	 			
  DMA_InitStructure.DMA_DIR 				= DMA_DIR_PeripheralDST;
  DMA_InitStructure.DMA_BufferSize 			= 24;  // uint16_t�ĳ���ΪΪ�ֽڵ�2����10�����ּ�20���ֽڵĳ���				
  DMA_InitStructure.DMA_PeripheralInc 		= DMA_PeripheralInc_Disable;//DMA_PeripheralInc_Enable;//	
  DMA_InitStructure.DMA_MemoryInc 			= DMA_MemoryInc_Enable;	  
  DMA_InitStructure.DMA_PeripheralDataSize 	=DMA_PeripheralDataSize_Byte;
  DMA_InitStructure.DMA_MemoryDataSize 		= DMA_PeripheralDataSize_Byte;
  DMA_InitStructure.DMA_Mode 				=DMA_Mode_Normal;// DMA_Mode_Normal;	// DMA_Mode_Circular ;	
  DMA_InitStructure.DMA_Priority 			= DMA_Priority_High;
  DMA_InitStructure.DMA_M2M 				= DMA_M2M_Disable;//DMA_M2M_Enable;		
  
  DMA_Init(DMA1_Channel4, &DMA_InitStructure);
	DMA_ITConfig(DMA1_Channel4,DMA_IT_TC, ENABLE);  
}


/*****************************************************************   
*��������:  NVIC_Config   
*��������:   ����DMA���ж����ȼ�  
*���ʱ��:2013��12��1��  
*�޸�����              �汾��              �޸���              �޸�����  
*-----------------------------------------------------------------   
*   
******************************************************************/   
void NVIC_Config(void)  
{  
         NVIC_InitTypeDef NVIC_InitStructure;    
          
         //DMA���ȼ�          
         NVIC_PriorityGroupConfig(NVIC_PriorityGroup_3);  
         NVIC_InitStructure.NVIC_IRQChannel= DMA1_Channel4_IRQn;   
         NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority= 2;   
         NVIC_InitStructure.NVIC_IRQChannelSubPriority= 1;   
         NVIC_InitStructure.NVIC_IRQChannelCmd= ENABLE;   
         NVIC_Init(&NVIC_InitStructure);   
          
          
//         /*Configure one bit for preemption priority -------------------------------- */  
//         NVIC_PriorityGroupConfig(NVIC_PriorityGroup_0);  
//          
//         /*UART1 -------------------------------------------------------------------- */  
//         NVIC_InitStructure.NVIC_IRQChannel= USART1_IRQn;  
//         NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority= 0;  
//         NVIC_InitStructure.NVIC_IRQChannelSubPriority= 1;  
//         NVIC_InitStructure.NVIC_IRQChannelCmd= ENABLE;  
//         NVIC_Init(&NVIC_InitStructure);     
//          
}  


void uart_sendInt(uint16_t sendData)
{
   union int_char{
	  int intA;
	  char charB[2];
 
   } int_Char;
  
		int_Char.intA =sendData;
	 
	 	USART_SendData(USART1,int_Char.charB [1]);
	while(USART_GetFlagStatus(USART1, USART_FLAG_TXE) == RESET){} //
		//printf("%d",dest[i]);//ֻ�����ַ�����ʽ����
		
	USART_SendData(USART1,int_Char.charB [0]);
	while(USART_GetFlagStatus(USART1, USART_FLAG_TXE) == RESET){} //
	
	
}

